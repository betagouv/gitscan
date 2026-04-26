## Changelog : git-ai-trace (30 derniers jours, au 24 avril 2026)

### Résumé
Cette première version de `git-ai-trace` introduit un outil permettant d'intégrer un résumé de la collaboration entre l'humain et l'IA dans les messages de commit Git.  Elle fournit les bases pour le suivi de l'évolution du code et la contribution de chaque partie, avec une configuration initiale pour le CI/CD et la publication.

### Évolutions fonctionnelles
- Ajout des hooks Git pour intégrer le résumé de la collaboration IA/humain dans les messages de commit.
- Publication initiale de l'outil `git-ai-trace` et de ses hooks. [#8613a61](https://github.com/SocialGouv/git-ai-trace/commit/8613a61)

### Évolutions techniques
- Mise en place d'un pipeline CI/CD complet avec les workflows `release`, `tests` et `version`. [#c717ebe](https://github.com/SocialGouv/git-ai-trace/commit/c717ebe)
- Intégration d'outils de release (pnpm, release-it, build-skill.sh) pour automatiser le processus de publication. [#dbbf069](https://github.com/SocialGouv/git-ai-trace/commit/dbbf069)
- Suppression d'une commande `cat` inutile dans le hook `commit-msg` pour améliorer la performance et la lisibilité. [#61fa268](https://github.com/SocialGouv/git-ai-trace/commit/61fa268)
- Correction du lien vers le brainstorming dans les métadonnées. [#7033f13](https://github.com/SocialGouv/git-ai-trace/commit/7033f13)

### Autres changements
- Refonte du fichier README pour clarifier la provenance du projet.
- Ajout des fichiers `CONTRIBUTING` et `design-rationale` pour encourager la collaboration et documenter les choix de conception. [#51d5be8](https://github.com/SocialGouv/git-ai-trace/commit/51d5be8)
- Publication de la version v0.2.0. [#2018c5a](https://github.com/SocialGouv/git-ai-trace/commit/2018c5a)
