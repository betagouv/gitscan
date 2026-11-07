# Synthèse d'activité : demarche-numerique (du 25/10 au 31/10)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des capacités d'extraction de données et une amélioration significative de l'accompagnement des usagers. L'outil [la_taupe](/repos/demarche-numerique/la_taupe) gagne en précision et en efficacité pour le traitement automatisé des RIB, tandis que la documentation [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr) se structure avec le lancement d'un nouveau guide usager.

Parallèlement, la plateforme principale [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) renforce sa robustesse et sa sécurité, et le proxy [ds_proxy](/repos/demarche-numerique/ds_proxy) étend ses capacités de stockage vers des solutions comme S3. Enfin, l'écosystème s'élargit avec l'initialisation de nouveaux espaces de collaboration.

## Sécurité
- Renforcement de la sécurité des comptes "Super Admin" via l'enrôlement OTP et le verrouillage automatique dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Implémentation d'un sandboxing pour le traitement sécurisé des images via libvips dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Optimisation de l'extraction de données :** Passage à un nouveau moteur OCR (PP-OCR v6 tiny) et mise en place d'outils de benchmarking pour [la_taupe](/repos/demarche-numerique/la_taupe).
- **Évolutions d'infrastructure et de stockage :** 
    - Extension de la compatibilité de stockage (S3 et Swift) pour [ds_proxy](/repos/demarche-numerique/ds_proxy).
    - Migration vers Sidekiq 8 pour la gestion des tâches de fond dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Lancement de projets :** Initialisation des espaces d'échange et de collaboration via [commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr) et [commun-demarche-numerique](/repos/demarche-numerique/commun-demarche-numerique).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Amélioration de la précision de l'OCR et ajout du traitement par lots (batch).
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Évolutions fonctionnelles pour les instructeurs, renforcement de la sécurité et migrations techniques.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Extension des capacités de stockage et simplification des dépendances.
- [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr) : Structuration de la documentation et lancement du guide usager.
