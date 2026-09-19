# Synthèse d'activité : demarche-numerique (du 01/09 au 07/09)

## Résumé de l'activité
L'activité récente est marquée par une modernisation profonde de la plateforme principale [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), tant sur le plan de l'expérience utilisateur (gestion des fichiers, recherche) que de l'infrastructure. Parallèlement, l'outil d'extraction [la_taupe](/repos/demarche-numerique/la_taupe) gagne en précision et en productivité grâce à l'intégration d'un nouveau moteur OCR et à la possibilité de traiter des documents par lots.

Enfin, l'écosystème s'enrichit avec le lancement du projet de documentation V2 [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr) et une meilleure compatibilité de stockage pour le proxy [ds_proxy](/repos/demarche-numerique/ds_proxy).

## Sécurité
- Renforcement de la sécurité des comptes "Super Admin" et mise en place d'un registre de sessions sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Amélioration de la validation des jetons JWT sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- **Modernisation logicielle :** Migration de la plateforme vers Rails 8.1 et création d'un environnement sandbox sécurisé pour l'exécution de commandes sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- **Évolution de l'OCR :** Passage au moteur PP-OCR v6 pour une extraction de données (notamment les RIB) plus performante dans [la_taupe](/repos/demarche-numerique/la_taupe).
- **Interopérabilité de stockage :** Ajout du support pour S3 et Swift dans [ds_proxy](/repos/demarche-numerique/ds_proxy).
- **Lancement de projet :** Initialisation de la structure de la nouvelle documentation sur [doc-v2.demarche.numerique.gouv.fr](/repos/demarche-numerique/doc-v2.demarche.numerique.gouv.fr).

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Mise à jour majeure de la plateforme (infrastructure, sécurité et expérience utilisateur).
- [la_taupe](/repos/demarche-numerique/la_taupe) : Montée en puissance de l'extraction de données et du traitement par lots.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Extension des capacités de stockage et optimisation technique.
