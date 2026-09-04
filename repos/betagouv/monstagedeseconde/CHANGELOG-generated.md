## Changelog : monstagedeseconde (30 derniers jours, au 03/09/2026)

### Résumé
Cette période est marquée par l'introduction de la nouvelle interface chatMD, l'amélioration de la précision cartographique pour les détails des offres et un nettoyage important de l'interface (FAQ, modules tiers) afin de simplifier l'expérience utilisateur.

### Évolutions fonctionnelles
- Intégration de la nouvelle interface chatMD [#964](https://github.com/betagouv/monstagedeseconde/pull/964).
- Amélioration de la cartographie des offres grâce à l'utilisation de tuiles OSM France.
- Simplification de la FAQ par la suppression des anciens blocs de contenu [#966](https://github.com/betagouv/monstagedeseconde/pull/966).
- Refonte de l'organisation des espaces de la plateforme [#949](https://github.com/betagouv/monstagedeseconde/pull/949).

### Évolutions techniques
- Mise en place d'un "feature flip" pour permettre un déploiement contrôlé de chatMD.
- Correction d'un bug provoquant un plantage du helper de texte structuré Prismic sur la bannière supérieure.
- Refactorisation de la page des ressources.

### Autres changements
- Suppression du module Tally [#950](https://github.com/betagouv/monstagedeseconde/pull/950).
- Nettoyage de l'infrastructure et de l'environnement de test (suppression de Mailtrap et mise à jour de la clé CI).
