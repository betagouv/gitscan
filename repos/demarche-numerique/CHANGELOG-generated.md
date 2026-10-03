# Synthèse d'activité : demarche-numerique (du 14/09 au 21/09)

## Résumé de l'activité
L'activité de la période est marquée par une montée en puissance des capacités d'extraction de données et un renforcement de la fiabilité des services. L'outil [la_taupe](/repos/demarche-numerique/la_taupe) améliore significativement la précision de la lecture des RIB, facilitant ainsi le traitement automatisé des documents pour les utilisateurs. Parallèlement, la plateforme principale [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) gagne en résilience grâce à la mise en place de modes de fonctionnement dégradés et de nouveaux outils de gestion pour les instructeurs.

L'écosystème s'élargit également avec l'initialisation de nouveaux projets structurants, notamment pour la documentation [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr) et l'espace d'échange communautaire [commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr).

## Sécurité
- Renforcement de la sécurité des comptes Super Admin via l'authentification à usage unique (OTP) et une meilleure gestion des sessions dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Amélioration de la sécurité des API avec une validation accrue des URLs et des jetons JWT dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Amélioration de l'OCR et de l'extraction :** Passage à un nouveau moteur OCR plus performant et mise en place d'outils de mesure de précision (benchmarking) dans [la_taupe](/repos/demarche-numerique/la_taupe).
- **Évolutions d'infrastructure et de stockage :**
    - Extension des capacités de stockage avec le support de S3 et Swift dans [ds_proxy](/repos/demarche-numerique/ds_proxy).
    - Migration vers Sidekiq 8 pour la gestion des tâches de fond et implémentation d'un sandboxing pour le traitement d'images dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Lancement de nouveaux projets :** Initialisation des dépôts de documentation [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr) et de l'espace de partage [commun.demarche.numerique.gouv.fr](/repos/demarche-numerique/commun.demarche.numerique.gouv.fr).

## Dépôts les plus actifs
- [la_taupe](/repos/demarche-numerique/la_taupe) : Amélioration majeure de la précision de l'OCR et ajout du traitement par lots.
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Renforcement de la sécurité, de la résilience et des performances.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Évolution des capacités de stockage et optimisation technique.
