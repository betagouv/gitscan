# Synthèse d'activité : demarche-numerique (derniers 7 jours)

## Résumé de l'activité
L'organisation "demarche-numerique" a connu une semaine productive, axée sur l'amélioration de la plateforme principale [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) et de son infrastructure. Les utilisateurs bénéficieront d'une expérience plus stable avec la correction de bugs liés à la soumission de dossiers et à l'autosave. Des améliorations significatives en matière de sécurité ont été apportées, notamment la correction de vulnérabilités critiques et la migration vers une nouvelle gestion des sessions. Le proxy de chiffrement [ds_proxy](/repos/demarche-numerique/ds_proxy) a également été mis à jour pour faciliter son déploiement et sa maintenance.

## Sécurité
- Correction de plusieurs vulnérabilités de sécurité : SSRF, XSS, IDOR dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Migration vers une nouvelle méthode de gestion des sessions pour améliorer la sécurité et les performances dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- Refactoring important : remplacement de HAML par ERB pour améliorer la maintenabilité dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Utilisation de LightningCSS pour optimiser les performances du CSS dans [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Ajout d'un Dockerfile pour construire des images Docker publiques à partir du paquet Debian dans [ds_proxy](/repos/demarche-numerique/ds_proxy).

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Correction de bugs, améliorations de la sécurité et refactoring technique majeur pour une meilleure expérience utilisateur et maintenabilité.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Amélioration du processus de construction et de déploiement via l'ajout d'un Dockerfile.
