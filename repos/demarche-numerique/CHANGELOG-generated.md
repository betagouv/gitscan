# Synthèse d'activité : demarche-numerique (du 02/06 au 12/06)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) avec des ajouts fonctionnels pour faciliter la communication avec les utilisateurs (bannières administrables) et améliorer l'expérience de correction de demandes. Des efforts importants ont également été faits pour renforcer la sécurité de la plateforme, notamment concernant l'import CSV et l'API Entreprise, en y intégrant des mécanismes de protection contre les surcharges et les vulnérabilités. Enfin, des optimisations de performance ont été apportées à l'export de données.

## Sécurité
- Correction de vulnérabilités dans l'import CSV sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Ajout de circuit breakers et de rate limiting pour l'API Entreprise sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour une meilleure résilience et protection contre les abus.

## Autres changements notables
- Migration de composants HAML vers ERB sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour une meilleure maintenabilité du code.
- Utilisation de Redis pour la mise en cache de la configuration OIDC sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Correction d'un bug d'altération de l'en-tête `content-md5` lors du proxyage sur [ds_proxy](/repos/demarche-numerique/ds_proxy), assurant l'intégrité des fichiers.

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Amélioration significative de la plateforme avec des ajouts fonctionnels, des corrections de sécurité et des optimisations de performance.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Correction d'un bug critique affectant l'intégrité des données lors du proxyage HTTP.
