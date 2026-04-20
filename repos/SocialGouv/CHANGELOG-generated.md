# Synthèse d'activité : SocialGouv (derniers 7 jours)

## Résumé de l'activité
L'activité de SocialGouv au cours des 7 derniers jours a été marquée par des améliorations significatives sur plusieurs fronts. On observe une forte concentration sur l'amélioration de l'expérience utilisateur et la correction de bugs, notamment sur [code-du-travail-numerique](/repos/SocialGouv/code-du-travail-numerique) avec l'ajout d'une section actualités et l'amélioration de la recherche, et sur [vao](/repos/SocialGouv/vao) avec des améliorations du module d'agrément. Des efforts importants ont également été déployés pour la modernisation technique, avec des migrations vers des versions plus récentes de langages et de frameworks (Python, Django, Pnpm) sur [collecte-pro](/repos/SocialGouv/collecte-pro) et [revu](/repos/SocialGouv/revu), ainsi que l'ajout de nouvelles fonctionnalités et l'amélioration de la sécurité sur [domifa](/repos/SocialGouv/domifa) et [egapro](/repos/SocialGouv/egapro).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations en matière de sécurité :
- [domifa](/repos/SocialGouv/domifa) a mis en place un système de limitation de requêtes et renforcé ses règles de sécurité.
- [egapro](/repos/SocialGouv/egapro) a sécurisé la route de téléchargement S3 via un proxy et implémenté une infrastructure d'audit logging.
- [revu](/repos/SocialGouv/revu) a mis à jour la configuration `sealed-secrets` pour l'environnement de pré-production.

## Autres changements notables
- Migration vers Pnpm sur [revu](/repos/SocialGouv/revu) et [iterion](/repos/SocialGouv/iterion) pour une meilleure gestion des dépendances.
- Migration vers Python 3.14 et Django 5.2.13 sur [collecte-pro](/repos/SocialGouv/collecte-pro) pour une meilleure pérennité et sécurité.
- Migration de l'authentification vers JWT sur [egapro](/repos/SocialGouv/egapro).
- Refactorisation importante de l'architecture de [iterion](/repos/SocialGouv/iterion) pour améliorer la performance et la flexibilité.

## Dépôts les plus actifs
- [egapro](/repos/SocialGouv/egapro) : Ajout de la gestion des référents, de l'impersonnation d'entreprises et d'attestations PDF.
- [vao](/repos/SocialGouv/vao) : Amélioration du module d'agrément avec la gestion des messages, le renouvellement et l'interface back-office.
- [code-du-travail-numerique](/repos/SocialGouv/code-du-travail-numerique) : Ajout d'une section actualités et amélioration de la recherche.
- [iterion](/repos/SocialGouv/iterion) : Intégration de nouveaux agents d'IA et amélioration significative de l'éditeur visuel.
- [domifa](/repos/SocialGouv/domifa) : Ajout d'un système de limitation de requêtes et amélioration de la gestion des données.
