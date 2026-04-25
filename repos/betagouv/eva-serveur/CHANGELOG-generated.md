## Changelog : eva-serveur (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur pour les opérateurs de compétences (OPCO) et les administrateurs, notamment en ajoutant des tableaux de bord dédiés, en affinant la gestion des invitations et des structures, et en renforçant la sécurité. Des refactorings importants ont également été effectués pour améliorer la structure du code et préparer l'application à de futures évolutions.

### Évolutions fonctionnelles

*   Les comptes OPCO peuvent désormais accéder à un tableau de bord dédié avec des statistiques issues de Metabase.
*   Ajout d'une fonctionnalité d'invitation pour les structures administratives.
*   Possibilité pour les OPCO de gérer et d'associer des parcours types à leurs comptes.
*   Amélioration de l'affichage des campagnes dans le dashboard Eva Pro, notamment lorsqu'il y en a plusieurs.
*   Les utilisateurs OPCO ont un accès restreint à la navigation d'EVA.
*   Les administrateurs peuvent modifier les IDCC (identifiants conventions collectives) d’un OPCO.
*   Ajout d'une page dédiée pour les invitations invalides.
*   Possibilité de consulter les explications de comparaison des évaluations littératie et numératie.
*   Amélioration de l'affichage des alertes d'invitation avec le nom et l'adresse de la structure.
*   Les pistes de solutions disponibles renvoient vers le widget de l'inclusion.
*   Ajout d'une gestion de l'usage et de l'OPCO pour les structures administratives.

### Évolutions techniques

*   Refactorisation importante du code lié aux évaluations, avec introduction de nouvelles classes `DiagnosticPro` et `PassationBeneficiaire` pour une meilleure organisation et maintenabilité.
*   Migration du script I18n vers une dépendance npm.
*   Correction d'une vulnérabilité d'injection SQL dans `CollectionsEvenementsController`.
*   Correction d'une faille de sécurité sur TarteauCitronJS.
*   Mise à jour de Ruby et Nodejs.
*   Suppression des progress bar Bootstrap au profit des composants DSFR.
*   Remplacement de Nominatim par geo.api.gouv.fr pour la géolocalisation des structures.
*   Amélioration du fichier CircleCI avec la mise en cache de libvips et l'augmentation des timeouts.
*   Passage de la modal d'acceptation des CGU et de vérification de compte en attente en DSFR pour supprimer l'utilisation de Bootstrap modal.
*   Suppression des modals Bootstrap et de leurs fichiers associés.
*   Anonymisation du SIRET des structures et des bénéficiaires supprimés.
*   Refactorisation des présentateurs de risques et de coûts dans le modèle `DiagnosticPro`.
*   Suppression du recaptcha.

### Autres changements

*   Harmonisation du wording « rejoindre une structure existante ».
*   Correction de bugs mineurs liés à l'affichage, aux marges, aux boutons et aux URLs.
*   Amélioration de la gestion des images dans les formulaires.
*   Ajout de tests unitaires pour valider les nouvelles fonctionnalités et les refactorings.
*   Mise à jour des dépendances.
*   Correction de l'affichage des actualités et des comptes sur EvaPro.
*   Correction des références à 'focus-incoutournable' en 'focus-incontournable' et changement d'image.
*   Suppression de code obsolète.
*   Ajout de classes CSS pour le logo dans le header EVA.
*   Mise à jour de la documentation.
*   Passage de l'application en Marianne et suppression des anciennes fonts.
*   Correction du visuel des actualités.
*   Correction de la position des boutons du header version mobile.
*   Correction du background hover des boutons.
*   Correction de la taille des boutons.
*   Correction du composant BoutonDSF.
*   Correction des hover secondary et tertiary.
*   Correction de l'affichage des campagnes dans le dashboard Eva pro quand il y en a plusieurs.
*   Correction des url des restitutions eva pro.
*   Correction des marges entre le Header/Contenu et Contenu/footer sur l'ensemble des pages.
*   Correction du scroll horizontal sur les pages listes evapro (vues admin).
*   Correction du double soulignement du lien de l'email dans la recherche de structure dans l'onboarding.
*   Correction du background de la modal qui ne prennait pas toute la fenetre.
*   Correction du hover du bouton close de la modal confirmation creation structure.
*   Correction de la taille des boutons.
*   Correction de l'affichage des campagnes dans le dashboard Eva pro quand il y en a plusieurs.
*   Correction des références à 'focus-incoutournable' en 'focus-incontournable' et changement d'image.
*   Correction du visuel des actualités.
*   Correction de la modale d'invitation.
*   Correction de la position des boutons du header version mobile.
*   Correction du background hover des boutons.
*   Correction de la taille des boutons.
*   Correction du composant BoutonDSF.
*   Correction des hover secondary et tertiary.
*   Correction de l'affichage des campagnes dans le dashboard Eva pro quand il y en a plusieurs.
*   Correction des références à 'focus-incoutournable' en 'focus-incontournable' et changement d'image.
*   Correction du visuel des actualités.
*   Correction de la modale d'invitation.
*   Correction de la position des boutons du header version mobile.
*   Correction du background hover des boutons.
*   Correction de la taille des boutons.
*   Correction du composant BoutonDSF.
*   Correction des hover secondary et tertiary.
*   Correction de l'affichage des campagnes dans le dashboard Eva pro quand il y en a plusieurs.
*   Correction des références à 'focus-incoutournable' en 'focus-incontournable' et changement d'image.
*   Correction du visuel des actualités.
*   Correction de la modale d'invitation.
*   Correction de la position des boutons du header version mobile.
*   Correction du background hover des boutons.
*   Correction de la taille des boutons.
*   Correction du composant BoutonDSF.
*   Correction des hover secondary et tertiary.
*   Correction de l'affichage des campagnes dans le dashboard Eva pro quand il y en a plusieurs.
*   Correction des références à 'focus-incoutournable' en 'focus-incontournable' et changement d'image.
*   Correction du visuel des actualités.
*   Correction de la modale d'invitation.
*   Correction de la position des boutons du header version mobile.
*   Correction du background hover des boutons.
*   Correction de la taille des boutons.
*   Correction du composant BoutonDSF.
*   Correction des hover secondary et tertiary.
*   Correction de l'affichage des campagnes dans le dashboard Eva pro quand il y en a plusieurs.
*   Correction des références à 'focus-incoutournable' en 'focus-incontournable' et changement d'image.
