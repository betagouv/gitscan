# Synthèse d'activité : france-connect (du 01/05 au 18/05/2026)

## Résumé de l'activité
L'activité récente de france-connect s'est concentrée sur l'amélioration de l'expérience utilisateur et de la sécurité de la plateforme. Des améliorations ont été apportées au tableau de bord utilisateur, notamment sur mobile, avec l'ajout d'un support pour de nouveaux prestataires via l'eIDASBridge et l'ajout d'un logo pour le futur IdP Yris. Des améliorations de la journalisation et de la traçabilité ont également été implémentées pour faciliter le diagnostic et la résolution des problèmes. Ces évolutions visent à offrir une expérience plus fluide et sécurisée aux utilisateurs finaux.

## Sécurité
- Ajout d'un message d'avertissement lorsque l'utilisateur désactive tous ses identifiants [sources](/repos/france-connect/sources).
- Séparation des consommateurs MongoDB par plateforme (FranceConnect niveau d'assurance faible et élevé) pour une meilleure isolation réseau [sources](/repos/france-connect/sources).

## Autres changements notables
- Refactorisation de la hiérarchie des dossiers pour améliorer le partage de code entre les applications React [sources](/repos/france-connect/sources).
- Suppression des claims inutilisés "phone_number" et "address" dans FranceConnect+ [sources](/repos/france-connect/sources).
- Ajout de contrôles de cache sur les routes de métadonnées [sources](/repos/france-connect/sources).
- Mise à jour des certificats de l'application local stack [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Amélioration continue de l'expérience utilisateur, de la sécurité et de la maintenabilité de la plateforme FranceConnect.
