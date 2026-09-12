# Synthèse d'activité : demarche-numerique (du 01/09 au 07/09)

## Résumé de l'activité
L'activité récente de l'organisation se concentre sur l'amélioration de la précision des outils de traitement et la modernisation des infrastructures. [la_taupe](/repos/demarche-numerique/la_taupe) gagne en efficacité grâce à un nouveau moteur d'OCR et une capacité de traitement par lots, facilitant l'extraction automatisée et robuste de données bancaires (RIB). [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) évolue également avec une interface plus fluide et de nouvelles capacités d'API pour une meilleure gestion des dossiers et de l'historique.

Enfin, l'écosystème gagne en flexibilité avec l'extension des capacités de stockage via [ds_proxy](/repos/demarche-numerique/ds_proxy) et pose les bases de la documentation de demain avec le lancement du projet [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr).

## Sécurité
- Renforcement de la sécurité contre les attaques par traversée de chemin (path traversal) lors de l'exportation de fichiers ZIP dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Migrations et architecture :**
    - Migration majeure de l'application principale vers Rails 8.1 dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
    - Refonte de l'architecture des champs via l'implémentation du polymorphisme (STI) dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
    - Optimisation des performances GraphQL pour réduire les requêtes N+1 dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Traitement de données et OCR :**
    - Passage au moteur PP-OCR v6 tiny pour une extraction de texte plus performante dans [la_taupe](/repos/demarche-numerique/la_taupe).
    - Mise en place d'un banc de mesure et d'outils de benchmarking pour évaluer la précision et la latence dans [la_taupe](/repos/demarche-numerique/la_taupe).
- **Infrastructure et stockage :**
    - Ajout de la prise en charge des protocoles de stockage S3 et Swift dans [ds_proxy](/repos/demarche-numerique/ds_proxy).
    - Simplification et allégement des dépendances pour améliorer la stabilité de [ds_proxy](/repos/demarche-numerique/ds_proxy).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Amélioration majeure de l'extraction de données RIB et de l'OCR.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Extension des capacités de stockage et optimisation des dépendances.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Migration vers Rails 8.1 et évolutions fonctionnelles de l'API et de l'interface.
- [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr) : Initialisation de la nouvelle documentation.
