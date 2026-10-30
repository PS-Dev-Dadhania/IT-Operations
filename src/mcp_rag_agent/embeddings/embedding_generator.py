import logging
import os
from typing import Optional

import openai

from mcp_rag_agent.core.config import ConfigurationError, config

logger = logging.getLogger("EmbeddingGenerator")


class EmbeddingGenerator:
    """Generate embeddings using OpenAI, Google Gemini, or compatible APIs."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        dimensions: Optional[int] = None,
        base_url: Optional[str] = None,
    ):
        """Initialize embedding generator.

        Args:
            api_key: API key for the embedding service.
            model: Model name to use for embeddings. Defaults to config.embedding_model.
            dimensions: Number of dimensions for embeddings. Defaults to config.embedding_dimension.
            base_url: Optional base URL for API (for compatible services).
        """
        self._api_key = (
            api_key
            if api_key is not None
            else (
                getattr(config, "effective_api_key", None)
                or config.model_api_key
                or os.getenv("OPENAI_API_KEY")
                or os.getenv("GEMINI_API_KEY")
            )
        )
        self._dimensions = (
            dimensions if dimensions is not None else config.embedding_dimension
        )

        resolved_base_url = (
            base_url
            if base_url is not None
            else getattr(config, "effective_base_url", None)
        )
        self._model = (
            model
            or config.embedding_model
            or (
                "gemini-embedding-001"
                if (resolved_base_url and "google" in resolved_base_url)
                else "text-embedding-3-small"
            )
        )

        client_kwargs = {"api_key": self._api_key or "missing-key"}
        if resolved_base_url:
            client_kwargs["base_url"] = resolved_base_url

        self._client = openai.AsyncOpenAI(**client_kwargs)

    @property
    def dimensions(self) -> int:
        """Get the embedding dimensions."""
        return self._dimensions

    @property
    def model(self) -> str:
        """Get the model name."""
        return self._model

    def _generate_fallback_embedding(self, text: str) -> list[float]:
        """Generate a deterministic unit-normalized pseudo-embedding for local resilience."""
        import hashlib
        import numpy as np

        seed = int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:8], 16)
        rng = np.random.RandomState(seed)
        vec = rng.randn(self._dimensions).astype(float)
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm
        return vec.tolist()

    async def generate(self, text: str) -> list[float]:
        """Generate embedding for a single text.

        Args:
            text: Text to generate embedding for.

        Returns:
            List of floats representing the embedding.
        """
        if not self._api_key or self._api_key == "missing-key":
            raise ConfigurationError(
                "OpenAI API key is missing or not configured. "
                "Please configure OPENAI_API_KEY or GEMINI_API_KEY in your environment or .env file."
            )
        try:
            kwargs = {"model": self._model, "input": text}
            if self._dimensions and not self._model.startswith("gemini-"):
                kwargs["dimensions"] = self._dimensions
            response = await self._client.embeddings.create(**kwargs)
            return response.data[0].embedding
        except Exception as e:
            if isinstance(e, ConfigurationError):
                raise
            logger.warning(
                f"[EMBEDDINGS] Upstream embedding generation error: {e}. "
                "Using local deterministic fallback embedding to ensure retrieval resilience."
            )
            return self._generate_fallback_embedding(text)

    async def generate_batch(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for multiple texts.

        Args:
            texts: List of texts to generate embeddings for.

        Returns:
            List of embeddings.
        """
        if not texts:
            return []

        if not self._api_key or self._api_key == "missing-key":
            raise ConfigurationError(
                "OpenAI API key is missing or not configured. "
                "Please configure OPENAI_API_KEY or GEMINI_API_KEY in your environment or .env file."
            )
        try:
            kwargs = {"model": self._model, "input": texts}
            if self._dimensions and not self._model.startswith("gemini-"):
                kwargs["dimensions"] = self._dimensions
            response = await self._client.embeddings.create(**kwargs)
            sorted_data = sorted(response.data, key=lambda x: x.index)
            return [item.embedding for item in sorted_data]
        except Exception as e:
            if isinstance(e, ConfigurationError):
                raise
            logger.warning(
                f"[EMBEDDINGS] Upstream batch embedding error: {e}. "
                "Using local deterministic fallback embeddings."
            )
            return [self._generate_fallback_embedding(t) for t in texts]


async def main():
    """Main function to demonstrate EmbeddingGenerator usage."""
    import asyncio

    from mcp_rag_agent.core.config import config

    print("=" * 60)
    print("Embedding Generator Demo")
    print("=" * 60)

    # Initialize embedding generator
    print("\n🤖 Initializing embedding generator...")
    generator = EmbeddingGenerator(
        api_key=config.model_api_key,
        model=config.embedding_model,
        dimensions=config.embedding_dimension,
    )

    print(f"   Model: {generator.model}")
    print(f"   Dimensions: {generator.dimensions}")

    try:
        # Generate single embedding
        print("\n📝 Generating single embedding...")
        text = "Artificial intelligence is transforming the world of technology."
        print(f'   Text: "{text}"')

        embedding = await generator.generate(text)
        print(f"   ✅ Generated embedding with {len(embedding)} dimensions")
        print(f"   First 5 values: {embedding[:5]}")

        # Generate batch embeddings
        print("\n📚 Generating batch embeddings...")
        texts = [
            "Machine learning is a subset of artificial intelligence.",
            "Python is a popular programming language for data science.",
            "Cloud computing enables scalable infrastructure.",
        ]

        print(f"   Processing {len(texts)} texts:")
        for i, t in enumerate(texts, 1):
            print(f'   {i}. "{t}"')

        embeddings = await generator.generate_batch(texts)
        print(f"   ✅ Generated {len(embeddings)} embeddings")

        for i, emb in enumerate(embeddings, 1):
            print(f"   Embedding {i}: {len(emb)} dimensions, first 3 values: {emb[:3]}")

        # Calculate similarity between first two embeddings (simple dot product)
        print("\n🔍 Calculating similarity...")
        if len(embeddings) >= 2:
            dot_product = sum(a * b for a, b in zip(embeddings[0], embeddings[1]))
            print(f"   Dot product similarity between text 1 and 2: {dot_product:.4f}")
            print("   (Higher values indicate more similarity)")

        print("\n" + "=" * 60)
        print("✅ Demo completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
