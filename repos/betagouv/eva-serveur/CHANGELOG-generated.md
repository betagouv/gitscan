## Changelog : eva-serveur (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la sécurité, la modernisation de l'interface utilisateur avec le Design System de la République Française (DSFR), et l'ajout de fonctionnalités pour la gestion des OPCO et des structures, notamment en lien avec les parcours types. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Les employés d'OPCO ont désormais un accès restreint à la navigation d'EVA.
- Les structures administratives peuvent désormais être associées à un usage et un OPCO.
- Possibilité de consulter les explications de comparaison des évaluations littératie et numératie.
- Amélioration du parcours d'inscription avec la gestion des invitations et des structures existantes.
- Les super-admins peuvent maintenant créer des structures sans SIRET.
- Ajout de la gestion des parcours types pour les OPCO, permettant de les associer à des campagnes.
- Possibilité pour les super-admins de modifier les IDCC (identifiants conventions collectives) d’un OPCO.
- Ajout de la possibilité de supprimer le visuel de l'offre de services dans le modèle Opco.
- Les administrateurs peuvent modifier le SIRET d'une structure même s'il est en doublon.
- Amélioration de la gestion des structures lors de l'inscription en cas de doublon de SIRET.
- Ajout d'une page dédiée pour les invitations invalides.
- Possibilité de créer une campagne lors de la création d'une structure.
- Les utilisateurs peuvent désormais enregistrer le numéro de téléphone lors de la création d'un compte lors de l'embarquement.

### Évolutions techniques
- Migration du script I18n vers une dépendance npm.
- Mise à jour de Ruby et Nodejs.
- Refactorisation de la gestion des mises en action dans le modèle `Evaluation` avec l'introduction de la classe `PassationBeneficiaire`.
- Remplacement de Nominatim par geo.api.gouv.fr pour la géolocalisation des structures.
- Utilisation du Design System de la République Française (DSFR) pour les boutons et les composants d'interface utilisateur, remplaçant Bootstrap.
- Amélioration de la configuration de la CI/CD avec la mise en cache de libvips et l'augmentation des timeouts.
- Suppression de code obsolète (modals Bootstrap, fichiers CSS inutilisés).
- Correction d'une vulnérabilité d'injection SQL dans `CollectionsEvenementsController`.
- Correction d'une faille de sécurité sur TarteauCitronJS.
- Anonymisation du SIRET des structures et des bénéficiaires supprimés.
- Actualisation des dépendances (Rails, ActiveAdmin, Devise, etc.).
- Refactorisation du code pour améliorer la cohérence et la structure.

### Autres changements
- Correction de divers problèmes d'affichage et de style (actualités, index des comptes EvaPro, PDF de comparatifs bénéficiaire).
- Amélioration de la gestion des alertes et des messages d'information.
- Ajout de tests unitaires et d'intégration.
- Configuration de Plausible pour tracer les liens sortants.
- Correction de bugs mineurs et amélioration de l'expérience utilisateur.
- Harmonisation du wording de certains éléments de l'interface utilisateur.
- Correction de problèmes de responsive design.
- Suppression des progress bars Bootstrap.
- Correction du scroll horizontal sur les pages listes evapro (vues admin).
- Correction du visuel des actualités.
- Correction de la modale d'invitation.
- Correction du placeholder du select Role dans la modal d'invitation.
- Correction des marges entre le Header/Contenu et Contenu/footer sur l'ensemble des pages.
- Correction des URL des restitutions eva pro.
- Correction des padding.
- Correction des bugs liés à la gestion des images.
- Correction des boutons et liens.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de commentaires et documentation.
- Suppression de code inutilisé.
- Correction des références à 'focus-incoutournable' en 'focus-incontournable'.
- Modification de la condition d'affichage des campagnes pour exclure les structures EVAPRO dans la vue des détails.
- Renommage de l'usage 'Eva: entreprises' en 'EVAPRO' dans l'ensemble de l'application.
- Correction du titre de la sidebar :responsable_de_suivi.
- Suppression du code de l'ancien menu mobile.
- Suppression d'une ligne d'habilitation inutile.
- Ajout de classes `DiagnosticPro` et `PassationBeneficiaire` pour gérer les évaluations.
- Ajout de nouvelles classes `ImpactsPresenter`, `RisquesPresenter`, `CoutsPresenter`, et `Restitution`.
- Ajout de la classe `TableauDeBordMisesEnAction` pour structurer les requêtes associées.
- Ajout de tests pour la methode departement de geoloc_helper.
- Fusion de cherche_region dans cherche_commune via l'API communes.
- Restauration du scope .near et correction des coordonnées dans les tests.
- Ajout du code commune dans la table structure.
- Enregistrement du code_commune à la création d'une structure.
- Les pistes de solutions disponibles renvoient vers le widget de l'inclusion.
- Ajout de la gestion de l'usage et de l'OPCO pour les structures administratives.
- Correction de la purge des comptes référencés dans des invitations.
- Correction du double soulignement du lien de l'email dans la recherche de structure dans l'onboarding.
- Géolocalisation et sauvegarde à la demande si code_commune est absent.
- Correction du visuel des actualités.
- Correction de la modale d'invitation.
- Correction de la soumission du formulaire de fusion des beneficaires.
- Correction du background de la modal qui ne prennait pas toute la fenetre.
- Correction du hover du bouton close de la modal confirmation creation structure.
- Correction de la taille des boutons.
- Correction du composant Rechercher ma structure.
- Correction des boutons du composant Rechercher ma structure.
- Correction des boutons annulé sur la partie active admin.
- Correction du bouton menu action.
- Correction des padding.
- Correction de la version petit ecran.
- Correction de la version pdf.
- Correction de la navigation en attente.
- Correction de la redirection lors d'une invitation déjà utilisée.
- Correction des ouvertures de modales.
- Correction des références à 'focus-incoutournable' en 'focus-incontournable' et change l'image.
- Correction de la condition d'affichage des campagnes pour exclure les structures EVAPRO dans la vue des détails.
- Ajout de la gestion des comptes en attente restreints dans le composant de navigation, et permet l'affichage des modals.
- Ajout des styles et des classes pour le logo dans le header EVA.
- Gère l'état actif pour les menus déroulants.
- Ajoute la possibilité de supprimer le visuel de l'offre de services dans le modèle Opco.
- Ajoute la possibilité de supprimer le visuel de l'offre de services dans le modèle Opco.
- Ajoute la possibilité de supprimer le visuel de l'offre de services dans le modèle Opco.
- Ajoute la possibilité de supprimer le visuel de l'offre de services dans le modèle Opco.
- Ajoute la possibilité de supprimer le visuel de l'offre de services dans le modèle Opco.
