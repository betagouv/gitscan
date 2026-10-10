# Synthèse d'activité : demarche-numerique (du 15/09 au 21/09/2026)

## Résumé de l'activité
L'activité de cette période est marquée par une montée en puissance des capacités d'extraction de données et une consolidation des outils de gestion. [la_taupe](/repos/demarche-numerique/la_taupe) franchit une étape clé avec un moteur d'OCR plus performant, permettant une lecture plus précise et automatisée des documents bancaires (RIB). Parallèlement, [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) se concentre sur l'amélioration de l'expérience des administrateurs et la robustesse des processus métier.

L'organisation amorce également de nouveaux chantiers structurants avec l'initialisation de projets dédiés à la documentation de nouvelle génération et à la création d'un espace d'échange pour l'ensemble de l'écosystème.

## Sécurité
- Renforcement de la sécurité des comptes "Super Admin" via l'enrôlement OTP et le verrouillage automatique sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Mise en place d'un sandboxing (via libvips) pour sécuriser le traitement des images sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Sécurisation des API par la validation des URLs et des jetons JWT sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Amélioration de l'OCR et du traitement de données :** Passage à un nouveau moteur d'OCR (PP-OCR v6 tiny) et ajout du traitement par lots (batch) via CLI pour [la_taupe](/repos/demarche-numerique/la_taupe).
- **Flexibilité du stockage :** Extension de la prise en charge des protocoles S3 et Swift pour [ds_proxy](/repos/demarche-numerique/ds_proxy).
- **Optimisation de l'infrastructure :** Migration vers Sidekiq 8 pour une meilleure gestion des tâches de fond sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Lancement de nouveaux projets :** Initialisation des dépôts pour la nouvelle documentation ([doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr)) et l'espace de partage communautaire ([commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr)).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Évolutions majeures sur la précision de l'extraction des données bancaires et les performances de l'OCR.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Améliorations fonctionnelles pour les instructeurs et renforcement de la sécurité applicative.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Optimisation de la configuration et ajout de nouveaux types de stockage.
