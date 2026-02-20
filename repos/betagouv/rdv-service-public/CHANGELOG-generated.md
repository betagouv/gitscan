## Changelog : rdv-service-public (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à rdv-service-public au cours des 30 derniers jours. Les principales évolutions concernent la synchronisation Caldav, la gestion des rendez-vous collectifs, la sécurité, et l'expérience utilisateur globale. Des corrections de bugs et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- Correction de l'affichage des noms des agents superposés (#6010).
- Amélioration de l'affichage des erreurs lors de la saisie du code de connexion (#6062).
- Permettre l'annulation d'une participation à un RDV collectif à l'initiative du service (#6127).
- Correction du lien de rdv d'accompagnement (#6149).
- Afficher les infos de contact d'une organisation si aucun créneaux n'est disponible (#6146).
- Amélioration de l'affichage des détails des rendez-vous (#6107).
- Correction de la suppression des login codes (#6151).
- Amélioration de l'affichage des prescripteurs sur les RDV collectifs (#6124).
- Ajout de la prise en charge des motifs de visioconférence pour l'API des créneaux (#6135).
- Correction de l'apparition de la recherche des plages d'ouvertures (#6054).
- Suppression du formulaire d’inscription usager (#6014).
- Correction d'une erreur 400 lors de la saisie d'un code de login erroné (#6061).
- Ajout d'une page d'erreur 400 plus informative (#6059).
- Amélioration de la homepage (#6084).
- Correction d'un bug empêchant l'affichage des indisponibilités Caldav sur l'agenda multi-agents (#6078).
- Amélioration de la gestion des événements récurrents Caldav (#6047).

### Évolutions techniques
- Passage à Yarn v4 (#6064).
- Passage de fullcalendar v5 à la v6 (#6080).
- Renforcement des mesures de sécurité CSP pour unpkg, mapbox et maplibre (#6156).
- Correction d'une vulnérabilité CVE 2026-26996 (#6157).
- Refactorisation de UserRdvWizard avant fusion des étapes (#6120).
- Amélioration de la gestion des attributs cassés dans Users::RdvBuilder (#6134).
- Suppression du flag SIGN_IN_AS_ALLOWED (#6138).
- Dépréciations de la synchronisation Webcal (#6060).
- Utilisation même wording agent introuvable et mot de passe incorrect (#6057).
- Suppression de la colonne `connected_with_agent_connect` (#6093).
- Suppression de la colonne `caldav_url` dans la table `Absences` (#6092).
- Mise à jour de Ruby vers la version 3.4.8 (#6032).
- Stockage des événements Caldav dans une table dédiée (#6031).
- Génération asynchrone du corps des webhooks (#6051).
- Amélioration de la gestion des erreurs 422 dans le client de migration inter-instances (#6044).
- Passage à Redis comme service dans le CI (#6112).
- Limitation du parallélisme dans le calculateur de créneau (#6095).

### Autres changements
- Suppression de l'utilisation de Headway pour la récupération des articles de blog, utilisation de docs.numerique.gouv.fr (#6024).
- Ajout de l'ID du FI ProConnect pour les agents (#6034).
- Correction de tests flaky (#6041).
- Ajout de Mehdi sur le PR reminder (#6042).
- Suppression de la connexion par mot de passe pour les agents ProConnectés (#6088).
- Correction de l'anonymizer (#6074).
- Ajout d’une erreur lorsqu’on essaye de créer une review app sans être connecté (#6126).
- Suppression de l'affichage de l'attribut alt pour le logo dans les emails (#6145).
- Amélioration de l'outillage multi-instance en local (#6143).
- Correction d'une flaky spec dans `import_absences_from_caldav_job_spec.rb` (#6147).
- Correction d'une flaky spec dans `find(".xdsoft_time", text: "14:15")` (#6132).
- Suppression de la colonne `caldav_url` dans la table `Absences` (#6092).
- Ajout d’une valeur pré-calculée pour déterminer si on demande la 2FA (#6055).
- Ajout de logging des appels Caldav à Sentry pour le débogage (#6066).
- Surveillance de l'exécution du Cron Job d'envoi des rappels via Sentry (#6045).
- Correction de la migration inter-instance pour les rendez-vous dont l'agent a été supprimé (#6094).
- Ajout de la synchronisation Caldav pour tous (fin du feature flag) (#6025).
- Correction de la gestion des erreurs lors de la synchronisation Caldav (#6075).
- Correction d'un crash lors du test de sectorisation (#6110).
- Amélioration de la liste des RDV d'un usager (#6053).
- Correction d'un crash lors du test de sectorisation (#6110).
- Suppression de la gem dotenv en environnement de production (#6125).
- Correction d'un bug lié à la séparation visuelle des colonnes de l'agenda (#6077).
- Ajout d'une vérification de l’accès en lecture et en écriture agenda CalDAV (#6148).
- Correction de l'affichage des erreurs lors de la saisie du code (#6062).
- Correction de la logique de fermeture d'une organisation quand on est le dernier administrateur de territoire (#6063).
- Correction de l'affichage des infos de contact d'une organisation si aucun créneau n'est disponible (#6146).
- Amélioration de l'affichage des prescripteurs sur les RDV collectifs (#6124).
- Correction d'un bug empêchant l'affichage des indisponibilités Caldav sur l'agenda multi-agents (#6078).
- Ajout d’une erreur lorsqu’on essaye de créer une review app sans être connecté (#6126).
- Suppression de l'affichage de l'attribut alt pour le logo dans les emails (#6145).
- Amélioration de l'outillage multi-instance en local (#6143).
- Correction d'une flaky spec dans `import_absences_from_caldav_job_spec.rb` (#6147).
- Correction d'une flaky spec dans `find(".xdsoft_time", text: "14:15")` (#6132).
- Ajout d’une valeur pré-calculée pour déterminer si on demande la 2FA (#6055).
- Ajout de logging des appels Caldav à Sentry pour le débogage (#6066).
- Surveillance de l'exécution du Cron Job d'envoi des rappels via Sentry (#6045).
- Correction de la migration inter-instance pour les rendez-vous dont l'agent a été supprimé (#6094).
- Ajout de la synchronisation Caldav pour tous (fin du feature flag) (#6025).
- Correction de la gestion des erreurs lors de la synchronisation Caldav (#6075).
- Correction d'un crash lors du test de sectorisation (#6110).
- Amélioration de la liste des RDV d'un usager (#6053).
- Correction d'un bug empêchant l'affichage des indisponibilités Caldav sur l'agenda multi-agents (#6078).
- Ajout d’une erreur lorsqu’on essaye de créer une review app sans être connecté (#6126).
- Suppression de l'affichage de l'attribut alt pour le logo dans les emails (#6145).
- Amélioration de l'outillage multi-instance en local (#6143).
- Correction d'une flaky spec dans `import_absences_from_caldav_job_spec.rb` (#6147).
- Correction d'une flaky spec dans `find(".xdsoft_time", text: "14:15")` (#6132).
- Ajout d’une valeur pré-calculée pour déterminer si on demande la 2FA (#6055).
- Ajout de logging des appels Caldav à Sentry pour le débogage (#6066).
- Surveillance de l'exécution du Cron Job d'envoi des rappels via Sentry (#6045).
- Correction de la migration inter-instance pour les rendez-vous dont l'agent a été supprimé (#6094).
- Ajout de la synchronisation Caldav pour tous (fin du feature flag) (#6025).
- Correction de la gestion des erreurs lors de la synchronisation Caldav (#6075).
- Correction d'un crash lors du test de sectorisation (#6110).
- Amélioration de la liste des RDV d'un usager (#6053).
