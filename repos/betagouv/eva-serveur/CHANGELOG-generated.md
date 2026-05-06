## Changelog : eva-serveur (30 derniers jours, au 5 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur avec une migration progressive vers le Design System FR (DSFR) pour une meilleure cohérence visuelle et accessibilité. Des corrections de bugs et des optimisations ont été apportées, notamment concernant la gestion des invitations, des structures, des OPCO et des PDF. La géolocalisation des structures a été améliorée avec l'utilisation de l'API gouvernementale geo.api.gouv.fr.

### Évolutions fonctionnelles
- Ajout d'une page dédiée pour les invitations invalides. [#76dbc5f](https://github.com/betagouv/eva-serveur/commit/76dbc5f)
- Les comptes en attente sont maintenant correctement affichés dans la section `/comptes`.
- Les invitations en attente sont filtrées correctement pour une structure donnée.
- Les OPCO peuvent accéder à un dashboard avec les statistiques Metabase. [#fb0e5ce](https://github.com/betagouv/eva-serveur/commit/fb0e5ce)
- Possibilité pour les structures administratives d'inviter des utilisateurs. [#df967f4](https://github.com/betagouv/eva-serveur/commit/df967f4)
- Les pistes de solutions disponibles renvoient vers le widget de l'inclusion.
- Amélioration de la gestion des usages et des OPCO pour les structures administratives. [#b6e142d](https://github.com/betagouv/eva-serveur/commit/b6e142d)
- Les bénéficiaires peuvent consulter les explications de comparaison des évaluations littératie et numératie.
- Ajout du calcul de la complétude des évaluations EVA Pro. [#8e02961](https://github.com/betagouv/eva-serveur/commit/8e02961)
- Correction de l'affichage des évaluations EVA Pro incomplètes. [#9e888c2](https://github.com/betagouv/eva-serveur/commit/9e888c2)
- Ajout d'un nouveau mode de calcul. [#d75dd25](https://github.com/betagouv/eva-serveur/commit/d75dd25)
- Affichage du logo de l'OPCO dans le header du PDF si l'OPCO est financeur.

### Évolutions techniques
- Migration progressive de l'interface utilisateur vers le Design System FR (DSFR).
- Remplacement de Nominatim par geo.api.gouv.fr pour la géolocalisation des structures.
- Suppression des utilities Bootstrap et remplacement par des équivalents DSFR.
- Refactorisation du code et ajout de tests pour améliorer la qualité et la maintenabilité.
- Amélioration de la configuration de la CI avec mise en cache de libvips.
- Mise à jour de Ruby et Nodejs.
- Correction d'une vulnérabilité d'injection SQL dans CollectionsEvenementsController.
- Renommage de l'usage 'Eva: entreprises' en 'EVAPRO' dans l'ensemble de l'application.
- Suppression de code obsolète (modals Bootstrap, fichiers CSS inutilisés).

### Autres changements
- Correction de divers problèmes de style et d'affichage sur mobile.
- Amélioration de la gestion des PDF (styles, impressions).
- Correction de bugs mineurs et améliorations de l'expérience utilisateur.
- Mise à jour de certaines dépendances.
- Correction de problèmes de focus sur Firefox.
- Suppression du numéro de téléphone de Gaelle.
- Ajout du code commune dans la table structure.
- Correction de l'URL des restitutions EVA Pro.
- Suppression de la modal de mise en garde et de ses traductions.
- Correction du titre de la sidebar :responsable_de_suivi.
- Suppression du code de l'ancien menu mobile.
- Ajout de Plausible pour tracer les outbound links.
- Correction de l'affichage des actualités et des comptes sur EvaPro.
- Correction des classes Bootstrap obsolètes.
- Correction de l'intégration des actualités.
- Correction d'un N+1 sur la page des actualités.
- Correction d'un bug sur les accès.
- Ajout de validations sur l'extension des fichiers audio.
- Amélioration du scroll horizontal sur les pages listes EVA Pro.
- Correction des marges entre le Header/Contenu et Contenu/footer sur l'ensemble des pages.
- Correction du double soulignement du lien de l'email dans la recherche de structure dans l'onboarding.
- Correction de la redirection pour les comptes ProConnect sans structure.
- Correction de la page Ma structure et de la page structure en mobile.
- Correction de la page mon compte sur mobile et de la page aide.
- Correction de l'interface de la page actualités sur mobile.
- Correction de la modale d'invitation.
- Correction de la page détail d'un bénéficiaire sur mobile.
- Correction de la modale du tableau de bord sur mobile.
- Correction du détail d'une actualité sur mobile.
- Correction du hover du breadcrumb.
- Correction du padding left des radio button d'activeadmin.
- Correction du visuel des actualités.
- Correction de la purge des comptes référencés dans des invitations.
- Correction de l'erreur 500 sur la page index Questionnaires.
- Correction du padding sur la version mobile.
- Correction du padding dans le PDF.
- Ajout d'un padding bottom pour les labels des forms.
- Ajout du logo EVAPRO dans la démonstration.
- Suppression du background des forms.
- Permettre au CMR de voir tous les comptes en lecture seule.
- Corrige les comptes en attente dans /comptes.
- Corrige un test aléatoire.
- Aligne les cards diagnostique par 3 sur le dashboard.
- Corrige le focus des boutons DSFR sur firefox.
- Corrige les classes bootstrap des utilities qui n'ont pas été converties pour utiliser le DSFR.
- Corrige un bug sur les select dans les filtres d'activeadmin.
- Corrige l'erreur 500 sur la page index Questionnaires.
- Corrige la partie mobile du contact opco dans evalutaion.
- Corrige la version petit ecran.
- Corrige la version pdf.
- Corrige les références à 'focus-incoutournable' en 'focus-incontournable' et change l'image.
- Corrige la condition d'affichage des campagnes pour exclure les structures EVAPRO dans la vue des détails.
- Corrige la condition pour exclure l'affichage des statistiques pour les structures EVAPRO dans la vue des détails.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
- Corrige le padding.
