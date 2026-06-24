## Changelog : rdv-service-public (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'intégration du Design System de la DINUM (DSFR) pour une interface plus cohérente et accessible. Des corrections de bugs et des améliorations de la synchronisation CalDAV ont également été apportées, ainsi que des optimisations concernant la gestion des services et des motifs de rendez-vous. La migration vers le nouveau nom de domaine rdv.numerique.gouv.fr a été finalisée.

### Évolutions fonctionnelles
- Les boutons et badges Bootstrap ont été remplacés par leurs équivalents DSFR, améliorant l'harmonie visuelle et l'accessibilité.
- Ajout d'une flèche sur les cartes de motifs pour améliorer leur visibilité et leur découvrabilité.
- Amélioration du message d'erreur pour les numéros de téléphone étrangers.
- Possibilité d'envoyer des emails avec le nouveau nom de domaine rdv.numerique.gouv.fr.
- Les agents de l'État sont automatiquement redirigés vers le nouveau domaine rdv.numerique.gouv.fr.
- Simplification du parcours de rendez-vous téléphonique.
- Ajout de l'email du bénéficiaire au parcours de prescription.
- Ajout d'instructions pour les usagers dans la réservation en ligne.
- Redirection vers la liste des créneaux collectifs après inscription d'un usager.
- Correction d'un lien raccourci pour accéder aux créneaux libres en file d'attente.
- Possibilité pour les admins d'espace de créer un nouveau service.
- Correction de l'annulation d'un rendez-vous.
- Suppression des rendez-vous d'accompagnement pour les espaces ouverts avec le compte opérateur.

### Évolutions techniques
- Mise à jour de Puma vers la version 7.2.1.
- Mise à jour de Bundler vers la version 4.0.12.
- Utilisation de la stack `scalingo-24` dans les review apps.
- Refactorisation pour préparer l'ajout d'intervalles après les rendez-vous.
- Suppression de code inutilisé et de commentaires obsolètes.
- Amélioration de la gestion des erreurs Caldav et ajout de debug à Sentry.
- Correction de flaky specs liées aux prénoms aléatoires et aux connections ActionCable.
- Suppression de la contrainte d'unicité sur `Service#short_name`.
- Limitation de la longueur des noms de service.
- Utilisation de cartes DSFR pour la recherche de créneaux côté agents et pour les choix de motifs de rendez-vous collectifs.
- Utilisation d'un accordéon DSFR pour les composants d'historique de version et de notifications.
- Ajout d'un service de suivi de la cohérence des listes de RDV affichées côté agent.
- Correction de l'usage de `cleanup_preserved_jobs_before_seconds_ago` (GoodJob).
- Correction d'un effet de bug sur le bouton "Annuler".
- Correction de la synchronisation CalDAV avec Zimbra.
- Ajout d’une étape de sélection agenda sync CalDAV.

### Autres changements
- Ajout de la feuille de route.
- Ajout de documentation pour debugger les réponses de l’API Espace Opérateur ANCT.
- Ajout de la possibilité de créer les catégories de motifs lorsque `ants_connectable` est activé dans la super admin.
- Ajout de la possibilité de créer 29 motifs France Service en un clic dans la super admin.
- Ajout de la variable d'environnement pour afficher les login codes sur les review apps.
- Mise à jour des mentions légales pour le nom de domaine de la dinum.
- Ajout de la possibilité d'utiliser des FS FranceConnect différents par domaine.
- Ajout de la possibilité d'utiliser des numéros de téléphone des DROM pour les organisations.
- Suppression d'un formulaire de création d'organisation inutilisé.
- Affichage du nom de l'usager connecté.
- Correction d'un bug empêchant l'envoi d'emails de réinitialisation de mot de passe.
- Ignorer les valeurs invalides injectées dans le formulaire de contact.
- Ajout d'un espace manquant dans le titre de page sur un motif.
- Ajout de tests pour ne pas filtrer les valeurs des attributs AR.
- Suppression des règles Metrics de Rubocop.
- Ajout d'un temps de battement après les rendez-vous.
- Correction d'un bug lié aux absences récurrentes sur plusieurs jours.
- Ajout d'une bannière de prescription externe.
- Correction de l’activation des données perso sync CalDAV.
- Correction de la demande d’ouverture de compte État.
- Suppression du namespace global (Tod::TimeOfDay).
- Ajout d'une étape de sélection agenda sync CalDAV.
- Correction de l’effet du bouton « Annuler » lors d’une annulation.
- Correction de la synchronisation CalDAV avec Zimbra.
- Ajout d’une étape de sélection agenda sync CalDAV.
