# Synthèse d'activité : suitenumerique (du 29 juin au 26 juillet 2026)

## Résumé de l'activité
La période récente a été marquée par des améliorations significatives en matière de sécurité, de fonctionnalités et d'expérience utilisateur à travers les différents projets de l'organisation. Plusieurs dépôts ont bénéficié de correctifs de sécurité importants, notamment concernant la gestion des vulnérabilités et la protection des données sensibles. Des fonctionnalités clés ont été ajoutées, comme le chiffrement de bout en bout pour les transferts de fichiers ([transfers](/repos/suitenumerique/transfers)), des filtres de recherche avancés dans Drive ([drive](/repos/suitenumerique/drive)), et l'intégration de la messagerie Matrix dans Hub ([hub](/repos/suitenumerique/hub)).  Des efforts importants ont également été consacrés à la modernisation technique, avec la migration de certains projets vers des technologies plus performantes comme Vite ([calendars](/repos/suitenumerique/calendars)) et l'automatisation des processus de développement et de déploiement.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour de sécurité importantes :

*   Correction d'une vulnérabilité dans `PyJWT` dans [people](/repos/suitenumerique/people).
*   Mise à jour de `Keycloak` dans [messages](/repos/suitenumerique/messages) pour corriger une vulnérabilité CERTFR.
*   Blocage des requêtes SSRF dans [file-scanner](/repos/suitenumerique/file-scanner).
*   Renforcement de la sécurité du traitement des données ICS dans [calendars](/repos/suitenumerique/calendars).
*   Chiffrement des données sensibles dans [accounts](/repos/suitenumerique/accounts).
*   Correction d'une vulnérabilité dans [drive](/repos/suitenumerique/drive) avec la mise à jour de dépendances.

## Autres changements notables
*   **Refonte de l'infrastructure SIP pour roomkit-visio** ([roomkit-visio](/repos/suitenumerique/roomkit-visio)) pour la connexion des équipements SIP et RNIS.
*   **Migration du frontend de Calendars vers Vite** ([calendars](/repos/suitenumerique/calendars)) pour améliorer les performances.
*   **Implémentation des endpoints OAuth 2.0 dans menshen** ([menshen](/repos/suitenumerique/menshen)) pour l'échange de jetons.
*   **Refonte du backend de Find** ([find](/repos/suitenumerique/find)) et correction de bugs.
*   **Amélioration significative de la gestion des RSVP dans Calendars** ([calendars](/repos/suitenumerique/calendars)).
*   **Intégration de la messagerie Matrix dans Hub** ([hub](/repos/suitenumerique/hub)).

## Dépôts les plus actifs
*   **ui-kit** ([ui-kit](/repos/suitenumerique/ui-kit)) : Ajout de nouveaux composants et améliorations de l'accessibilité.
*   **transfers** ([transfers](/repos/suitenumerique/transfers)) : Ajout du chiffrement de bout en bout et de l'analyse antivirus.
*   **st-home** ([st-home](/repos/suitenumerique/st-home)) : Corrections et améliorations de la robustesse du téléchargement des données SIRENE et DILA.
*   **st-deploycenter** ([st-deploycenter](/repos/suitenumerique/st-deploycenter)) : Gestion des droits d'accès et des services.
*   **st-ansible** ([st-ansible](/repos/suitenumerique/st-ansible)) : Amélioration du déploiement de La Suite Territoriale avec `st-cli`.
*   **drive** ([drive](/repos/suitenumerique/drive)) : Ajout de filtres de recherche avancés et améliorations de la performance.
*   **hub** ([hub](/repos/suitenumerique/hub)) : Intégration de la messagerie Matrix.
*   **calendars** ([calendars](/repos/suitenumerique/calendars)) : Refonte de la gestion des RSVP et migration vers Vite.
*   **accounts** ([accounts](/repos/suitenumerique/accounts)) : Amélioration de la sécurité et de la flexibilité de l'authentification.
*   **conversations** ([conversations](/repos/suitenumerique/conversations)) : Ajout d'un indicateur d'impact carbone et refonte du backend.
