# Synthèse d'activité : demarche-numerique (du 01/07 au 21/09)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance de la fiabilité des outils de traitement de données et une amélioration de la résilience des services. [la_taupe](/repos/demarche-numerique/la_taupe) a franchi une étape clé avec un moteur d'OCR plus performant, permettant une extraction plus précise des informations bancaires (RIB), tandis que [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) a renforcé sa robustesse face aux indisponibilités de services externes.

Parallèlement, l'écosystème s'étend avec l'initialisation de nouveaux projets structurants, notamment la documentation de la version 2 ([doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr)) et un espace dédié aux échanges communautaires ([commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr)).

## Sécurité
- Renforcement de la sécurité des accès pour les administrateurs via la généralisation de ProConnect dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Sécurisation du traitement des fichiers par l'introduction d'un bac à sable (sandbox) et durcissement de la validation des URLs dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Optimisation de l'extraction de données :** Passage à un nouveau moteur OCR (PP-OCR v6 tiny) et mise en place d'outils de benchmarking pour garantir la précision de l'extraction dans [la_taupe](/repos/demarche-numerique/la_taupe).
- **Évolutions de l'infrastructure et du stockage :** Extension de la compatibilité avec les protocoles S3 et Swift, et simplification des dépendances dans [ds_proxy](/repos/demarche-numerique/ds_proxy).
- **Refonte technique de la plateforme :** Modernisation du moteur de recherche (PostgreSQL `tsvector`), migration des templates (HAML vers ERB) et optimisation des performances de requêtes dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Lancement de nouveaux projets :** Initialisation des dépôts de documentation ([doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr)) et de l'espace de partage communautaire ([commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr)).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Amélioration majeure de la précision de l'OCR et ajout du traitement par lots.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Évolutions de sécurité, de performance et d'accessibilité de la plateforme principale.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Amélioration de la flexibilité du stockage et optimisation technique.
