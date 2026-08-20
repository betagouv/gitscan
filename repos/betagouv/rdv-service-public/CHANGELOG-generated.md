## Changelog : rdv-service-public (30 derniers jours, au 19/08/2026)

### Résumé
Cette période est marquée par une amélioration significative de l'expérience des agents (nouveaux menus, gestion du planning, notifications) et l'introduction de la visioconférence. Le projet a également bénéficié d'une modernisation technique majeure (passage à Rails 8) et d'optimisations de performance pour la gestion des données et des exports.

### Évolutions fonctionnelles
- **Gestion du planning et des rendez-vous** : Autorisation des rendez-vous les dimanches et jours fériés pour les admins de territoire [#6618], ajout d'un bouton "Nouveau" sur la page de planning [#6608], amélioration de l'affichage de la recherche de rendez-vous collectifs [#6617] et correction de la gestion des changements d'horaires pour les rendez-vous de suivi [#6599].
- **Expérience Agent** : Ajout d'un accès "Réservation en ligne" dans le menu agent [#6587], refonte du sélecteur d'organisation [#6568], affichage des invitations en attente dans le tableau des agents [#6588] et enrichissement du menu déroulant agent avec les paramètres du compte [#6549].
- **Notifications et communication** : Notification automatique des agents ajoutés à un rendez-vous [#6585], transfert des réponses usagers aux administrateurs des intervenants concernés [#6613] et amélioration des liens de reprise de rendez-vous via email et SMS [#6535].
- **Interface et Accessibilité** : Amélioration de l'accessibilité des liens utilisant uniquement des icônes [#6609], harmonisation de l'interface avec le DSFR (couleurs des motifs, modales de nouveautés) [#6582, #6578], mise à jour de la bibliothèque FullCalendar [#6506] et repositionnement du lien "Donnez votre avis" [#6548].
- **Nouvelles fonctionnalités** : Intégration de la visioconférence (Visio) [#6536] et affichage des informations de connexion FranceConnect dans le SuperAdmin [#6573].
- **Corrections diverses** : Correction de la saisie de durées négatives dans le wizard agent [#6530], de la prise de rendez-vous pour un autre agent [#6594] et de la recherche usager par numéro de téléphone [#4787077].

### Évolutions techniques
- **Modernisation du socle** : Mise à jour vers Rails 8.0.5.1 [#6572], migration de Sprockets vers Propshaft [#6576] et mise à jour de la gem `administrate` [#6519].
- **Optimisation et Base de données** : Nettoyage des colonnes inutilisées dans la table `users` [#6595, #6497], optimisation de l'empreinte mémoire des exports [#6597] et extraction de la configuration CalDAV dans une table dédiée [#6612].
- **Fiabilité et Monitoring** : Amélioration de la distinction des erreurs CalDAV sur Sentry [#6586], ajout de logs pour les paramètres des appels API [#6596] et réduction de l'instabilité des tests automatisés (remplacement des `sleep` par des `expect`) [#6533, #6534].
- **API et Intégration** : Corrections sur la gestion de CalDAV [#6621, #6615] et mise à jour des webhooks [#6592].

### Autres changements
- **Documentation** : Correction de la documentation pour visioplainte [#6607] et ajout de scripts pour le setup de machines virtuelles dédiées aux agents LLM [#6492].
