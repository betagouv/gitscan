## Changelog : eva-serveur (30 derniers jours, au 2026-05-15)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment une refonte avec le Design System Fr (DSFR) pour une meilleure cohérence et accessibilité. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des évolutions concernant la gestion des structures, notamment l'intégration des Opérateurs de Compétences (OPCO).

### Évolutions fonctionnelles
- Refonte de l'interface utilisateur avec le DSFR, incluant le parcours de réinitialisation du mot de passe.
- Affichage et filtrage du SIRET pour toutes les structures.
- Suppression du bouton copier/coller dans la modal d'invitation des structures OPCO et Administratives.
- Ajout de la possibilité d'accéder à la liste des structures OPCO.
- Ajout d'un dashboard pour les comptes OPCO avec les statistiques Metabase.
- Permet aux administrateurs de structures Administratives de ne pas accéder aux structures OPCO.
- Ajout de la fonctionnalité d'invitation pour les structures administratives.
- Les comptes OPCO ont désormais un accès restreint à la navigation d'EVA.
- Ajout d'une méthode pour calculer la complétude des évaluations EVAPRO.
- Permet de vider les comptes créés en démo, même invités.
- Ajout d'une migration pour créer les réponses "je ne sais pas" sur les questions des Impacts et risques.
- Amélioration de l'affichage des évaluations pour EvaPro.
- Correction de l'affichage de l'index compte sur EvaPro.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Devise, fast-uri, nokogiri, erb, postcss, net-imap.
- Suppression de la librairie geocoder.
- Suppression de plusieurs pages et actions obsolètes liées à la recherche et à la création de structures.
- Refactorisation de la logique de formatage du SIRET.
- Suppression de code mort concernant le rattachement des structures administratives à un OPCO.
- Migration des fichiers de localisation (I18n) vers une dépendance npm.
- Correction d'une vulnérabilité d'injection SQL dans CollectionsEvenementsController.
- Correction d'une faille de sécurité sur TarteauCitronJS.
- Mise à jour de Ruby et Nodejs.
- Suppression des utilities Bootstrap et migration vers le DSFR.
- Amélioration du cache dans le fichier CircleCI.
- Correction d'un N+1 sur la page des actualités.

### Autres changements
- Correction de tests aléatoires.
- Suppression d'attributs `aria-hidden` inutiles.
- Correction de bugs d'affichage et de rendu sur différentes pages (actualités, bénéficiaires, ma structure, etc.).
- Amélioration du design des PDF de comparatifs bénéficiaire en DSFR.
- Ajout de validations sur l'extension des fichiers audio dans le modèle Transcription.
- Ajout de commentaires et de documentation.
- Correction de problèmes de focus sur les boutons DSFR sur Firefox.
- Suppression de logs Capybara lors de l'exécution des tests.
- Correction de l'intégration du JS du DSFR pour éviter les erreurs en console.
- Correction du menu du DSFR.
- Suppression de la page 'structures'.
- Suppression de l'étape de prise en main 'Recherche structure'.
- Suppression du bouton 'ajouter une structure'.
- Suppression de la page 'admin/recherche_structure'.
- Ajout de mailers pour l'invitation de structures.
- Suppression de la page 'admin/sign_up'.
- Correction du lien d'invitation avec structure_id.
- Ajout de tests unitaires et fonctionnels.
- Amélioration de la gestion des erreurs.
- Correction de problèmes de padding et de marges.
- Suppression de progress bar Bootstrap.
- Ajout de placeholder pour le select Role dans la modal d'invitation.
- Suppression du numéro de téléphone de Gaelle.
- Ajustement du padding pour les labels des formulaires.
- Correction du padding mobile du contact OPCO dans l'évaluation.
- Correction du padding sur les pages listes EvaPro.
- Suppression de l'affichage des invitations en attente.
- Correction de l'affichage des actualités.
- Correction de l'affichage du tableau des évaluations.
- Correction du scroll horizontal sur les pages listes EvaPro.
- Correction de l'affichage des situations de Evapro incomplètes.
- Ajout d'une migration pour recalculer les données des évaluations EVAPRO.
- Ajout d'une méthode calcule_completude_evapro.
- Ajout d'un nouveau model StructureOpco.
- Renommage de la méthode vue_opco_active? en utilisateur_opco?.
- Ajout d'un padding de 16px sur la version mobile du tableau des évaluations eva.
- Ajout d'un test pour la methode vue_opco_active?.
- Création d'une methode est_une_structure_ocpo?.
- Ajout du dashboard operateur de competence dans la vue de detail d'une structure Operateur.
- Permet de creer ou de modifier une structure Operateur de competence.
- Permet d'accéder au show d'une structure Operateur de competence.
- Ajout de la validation sur l'extention du fichier audio dans le model transcription.
- Ajout des statistiques structure pour l'integration des statistique metabase opco.
- Ajoute le nouveau mode de calcul.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
- Corrige le pading.
