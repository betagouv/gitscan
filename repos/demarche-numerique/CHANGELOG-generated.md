# Synthèse d'activité : demarche-numerique (du 15/08 au 21/08)

## Résumé de l'activité
L'activité récente de l'organisation se concentre sur la modernisation des infrastructures et l'amélioration de l'expérience utilisateur. La plateforme principale [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) a franchi des étapes clés avec une meilleure gestion des comptes et des outils d'édition enrichis, facilitant le parcours des usagers. 

En parallèle, les capacités d'automatisation ont été renforcées : [la_taupe](/repos/demarche-numerique/la_taupe) gagne en précision et en efficacité pour l'extraction de données bancaires, tandis que [ds_proxy](/repos/demarche-numerique/ds_proxy) étend sa polyvalence en intégrant de nouveaux modes de stockage.

## Sécurité
- Renforcement de la protection contre les attaques par traversée de chemin (path traversal) dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Sécurisation de la traçabilité des messages de modification de dossier pour [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Migrations et architecture :**
    - Migration majeure vers Rails 8.1 pour [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
    - Refonte de l'architecture des formulaires via le polymorphisme et optimisation des performances (requêtes N+1) sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Évolutions technologiques :**
    - Passage à un nouveau moteur d'OCR (PP-OCR v6) plus performant pour [la_taupe](/repos/demarche-numerique/la_taupe).
    - Extension du support de stockage avec l'ajout de S3 et Swift pour [ds_proxy](/repos/demarche-numerique/ds_proxy).
    - Simplification et allégement des dépendances AWS pour [ds_proxy](/repos/demarche-numerique/ds_proxy).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Amélioration de la précision de l'extraction de données RIB et ajout du traitement par lots via CLI.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Extension des capacités de stockage et optimisation de la configuration.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Évolutions fonctionnelles majeures (fusion de comptes, API v2) et migration technique vers Rails 8.1.
