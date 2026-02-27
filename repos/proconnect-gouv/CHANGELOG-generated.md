# Synthèse d'activité : proconnect-gouv (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de l'expérience utilisateur et la maintenance technique de ses différents services. Plusieurs dépôts ont bénéficié de refontes d'interface, comme [federation](/repos/proconnect-gouv/federation) et [proconnect-identite](/repos/proconnect-gouv/proconnect-identite), avec une nouvelle présentation et des fonctionnalités améliorées pour les utilisateurs et les mairies. Des corrections de bugs et des optimisations de performance ont été apportées à plusieurs dépôts, notamment [hyyypertool](/repos/proconnect-gouv/hyyypertool) et [federation](/repos/proconnect-gouv/federation), pour une meilleure stabilité et fiabilité. L'accent a également été mis sur la sécurité avec l'ajout d'un fichier de politique de sécurité dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et des mises à jour de dépendances régulières.

## Sécurité
- Ajout d'un fichier `SECURITY.md` pour la politique de sécurité et la signalisation de vulnérabilités dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Mises à jour de dépendances dans plusieurs dépôts (voir sections ci-dessous) pour bénéficier des dernières corrections de sécurité.

## Autres changements notables
- Refonte importante des "guards" (sécurité) dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Suppression du fichier manifest.webmanifest trompeur dans [federation](/repos/proconnect-gouv/federation).
- Migration de la vérification "small association" vers le domaine dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).

## Dépôts les plus actifs
- [federation](/repos/proconnect-gouv/federation) : Refonte de l'interface utilisateur et corrections de bugs pour améliorer la stabilité et la performance.
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de l'interface utilisateur, ajout de nouvelles fonctionnalités pour les mairies et refactorisation de la sécurité.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Amélioration de l'accessibilité, corrections de bugs et intégration de Sentry pour un meilleur suivi des erreurs.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Intégration de Microsoft Entraid et mises à jour des dépendances.
