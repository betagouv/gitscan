# Synthèse d'activité : proconnect-gouv (du 09 mai 2026 au 16 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de l'expérience utilisateur et la robustesse des services existants. Plusieurs dépôts ont bénéficié de corrections de bugs et d'ajouts de fonctionnalités, notamment concernant la gestion des identités, la surveillance des services et l'intégration avec des standards comme eIDAS. L'ajout d'une page de maintenance et l'amélioration de la documentation pour les partenaires sont également des points forts de cette période. Le dépôt [class-validator](/repos/proconnect-gouv/class-validator) a connu une activité importante avec l'ajout de nouveaux validateurs et des améliorations de sécurité.

## Sécurité
Le dépôt [class-validator](/repos/proconnect-gouv/class-validator) a bénéficié de mises à jour de dépendances corrigeant des vulnérabilités. Le dépôt [federation](/repos/proconnect-gouv/federation) a remplacé les cookies par des session cookies pour une meilleure sécurité.

## Autres changements notables
- Le dépôt [federation](/repos/proconnect-gouv/federation) a implémenté un pattern ping/pong pour les healthchecks du broker et ajouté des routes `livez` et `readyz` pour une meilleure surveillance.
- Le dépôt [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) a corrigé une fuite de mémoire et intégré des changements de version automatique via `changesets`.
- Le dépôt [hyyypertool](/repos/proconnect-gouv/hyyypertool) a entamé le remplacement des composants DSFR par une nouvelle thématique Tailwind CSS.
- Le dépôt [oidc2fer](/repos/proconnect-gouv/oidc2fer) a amélioré la configuration et la gestion des identifiants SIRET.

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de la robustesse, correction de fuites mémoire et ajout d'informations sur les effectifs des unités légales.
- [federation](/repos/proconnect-gouv/federation) : Amélioration de la surveillance, de la sécurité et de la gestion des erreurs.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Amélioration de l'interface utilisateur et correction de bugs.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et amélioration de la sécurité.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Amélioration de la documentation et ajout d'une fonctionnalité de mode maintenance.
