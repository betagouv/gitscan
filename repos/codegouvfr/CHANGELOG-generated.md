# Synthèse d'activité : codegouvfr (derniers 7 jours)

## Résumé de l'activité
L'activité de codegouvfr au cours des dernières semaines a été marquée par des améliorations continues de ses outils et plateformes. Les efforts se sont concentrés sur l'amélioration de la gestion de la configuration et du déploiement avec [sill-deploy](/repos/codegouvfr/sill-deploy) et [catalogi](/repos/codegouvfr/catalogi), ainsi que sur la préparation d'une méthodologie d'évaluation des logiciels libres avec [floss-criteria](/repos/codegouvfr/floss-criteria). Des corrections de bugs et des améliorations de sécurité ont également été apportées à plusieurs dépôts, notamment [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) et [react-dsfr](/repos/codegouvfr/react-dsfr). Enfin, [cartonum](/repos/codegouvfr/cartonum) a vu l'ajout de nouvelles fonctionnalités axées sur la gestion documentaire et la sécurité.

## Sécurité
- Correction d'un bug dans [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) empêchant la redirection correcte vers la page d'autorisation en cas de client Keycloak inexistant.
- Plusieurs dépôts ([catalogi](/repos/codegouvfr/catalogi), [sill-deploy](/repos/codegouvfr/sill-deploy)) ont amélioré leur configuration de la politique de sécurité du contenu (CSP) pour autoriser l'affichage des images et le fonctionnement des workers Sentry, améliorant ainsi la sécurité et la robustesse des applications.

## Autres changements notables
- Migration de Yarn vers pnpm dans [catalogi](/repos/codegouvfr/catalogi) pour améliorer la performance et la cohérence de la gestion des dépendances.
- Utilisation de tsx pour le développement de l'API dans [catalogi](/repos/codegouvfr/catalogi) pour un rechargement à chaud plus rapide.
- Ajout de workflows de déploiement SILL dans [sill-deploy](/repos/codegouvfr/sill-deploy), synchronisant le dépôt avec l'upstream.
- Refactoring pour utiliser un modèle de packages internes pour le partage de types entre l'API et l'interface web dans [catalogi](/repos/codegouvfr/catalogi).

## Dépôts les plus actifs
- [cartonum](/repos/codegouvfr/cartonum) : Ajout de nouvelles fonctionnalités de gestion documentaire, de sauvegarde et d'infrastructure.
- [catalogi](/repos/codegouvfr/catalogi) : Amélioration de la gestion de la configuration et migration vers de nouveaux outils de gestion des dépendances.
- [sill-deploy](/repos/codegouvfr/sill-deploy) : Amélioration de la gestion de la configuration, intégration des workflows de déploiement SILL et corrections de l'interface web.
- [floss-criteria](/repos/codegouvfr/floss-criteria) : Début de la structuration des critères d'évaluation pour les logiciels libres.
