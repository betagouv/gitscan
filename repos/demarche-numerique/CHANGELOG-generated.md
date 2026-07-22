# Synthèse d'activité : demarche-numerique (du 30/06 au 06/07)

## Résumé de l'activité
La semaine a été marquée par des améliorations significatives sur la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), notamment l'ajout de l'OCR pour les avis d'imposition et une refonte de l'interface de recherche. Ces évolutions facilitent la gestion des pièces justificatives et améliorent l'expérience utilisateur, en particulier sur mobile.  Parallèlement, des optimisations techniques ont été apportées pour améliorer la performance et la sécurité de la plateforme. [ds_proxy](/repos/demarche-numerique/ds_proxy) a également bénéficié d'améliorations concernant la configuration et la gestion du stockage.

## Sécurité
- Renforcement de la sécurité des jetons API et correction de vulnérabilités potentielles sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Validation de la présence d'un jeton API Particulier sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- Début de la migration vers Rails 8 sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Refactorisation de la configuration S3 et simplification des dépendances sur [ds_proxy](/repos/demarche-numerique/ds_proxy).
- Ajout de la prise en charge de S3 et Swift avec détection automatique du type de stockage sur [ds_proxy](/repos/demarche-numerique/ds_proxy).

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Amélioration de l'expérience utilisateur avec l'OCR, la refonte de l'interface de recherche et des corrections de sécurité.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Amélioration de la flexibilité de la configuration et de la gestion du stockage, ainsi que des optimisations techniques.
