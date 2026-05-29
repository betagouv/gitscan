## Changelog : eva-serveur (30 derniers jours, au 28 mai 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des structures, notamment avec l'introduction des structures Opco et des modifications sur la recherche et l'invitation de structures. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, ainsi que des optimisations techniques et des mises à jour de dépendances.

### Évolutions fonctionnelles
- Ajout de la gestion des structures Opco : création, modification, affichage et accès via une nouvelle interface. [#6283553](https://github.com/betagouv/eva-serveur/commit/6283553)
- Possibilité de filtrer les structures par SIRET, avec une recherche tolérant les espaces.
- Restauration des fonctions d'autocomplétion pour la recherche de compte. [#db01108](https://github.com/betagouv/eva-serveur/commit/db01108)
- Affichage du SIRET pour toutes les structures.
- Amélioration de la gestion des invitations : correction des comptes créés en démo et des invitations en attente. [#f1b739f](https://github.com/betagouv/eva-serveur/commit/f1b739f)
- Ajout d'un indicateur de complétude des évaluations Evapro. [#73f5787](https://github.com/betagouv/eva-serveur/commit/73f5787)
- Affichage des liens vers les étapes dans les restitutions.
- Amélioration de l'affichage des restitutions EvaPro.
- Ajout d'URL officielles pour les compétences transversales.
- Possibilité de fermer la modale de validation en attente en cliquant sur le fond.
- Suppression des cadres superflus dans l'interface.
- Correction de l'affichage de l'index des évaluations pour EvaPro.

### Évolutions techniques
- Refactorisation du code pour le formatage du SIRET, avec création d'un helper pour éviter la duplication. [#8821b19](https://github.com/betagouv/eva-serveur/commit/8821b19)
- Suppression de code mort lié à l'ancien système de rattachement des structures administratives aux Opco.
- Migration des anciennes migrations de 2025 dans un dossier dédié.
- Mise à jour de la dépendance `jwt` vers la version 3.2.0. [#7ee913d](https://github.com/betagouv/eva-serveur/commit/7ee913d)
- Mise à jour du DSFR.
- Suppression de la bibliothèque `geocoder`.
- Suppression des pages et actions obsolètes liées à la recherche et à la création de structures.
- Suppression de la méthode `initCopierLienInvitation`.
- Déplacement des fichiers par type d'évaluation.
- Création d'un composant Metabase iframe pour les structures.
- Actualisation des dépendances JS.
- Suppression de classes CSS inutilisées.
- Suppression de l'utilisation des utilities Bootstrap au profit du DSFR.
- Amélioration de la gestion des erreurs et des tests.

### Autres changements
- Documentation de la variable d'environnement du tableau Metabase des Opco.
- Correction de linter sur un fichier CSS.
- Correction de l'affichage des bulles vertes sur les restitutions.
- Correction du focus des boutons DSFR sur Firefox.
- Suppression des fichiers `.pgsql` de la gestion de version.
- Ajout d'un nouveau modèle `StructureOpco`.
- Correction de l'affichage des actualités.
- Correction de l'intégration du JS du DSFR.
- Suppression des fichiers de cartes inutilisés.
- Correction de l'affichage du menu DSFR.
- Cache des logs Capybara lors de l'exécution des tests.
- Ajout de tests pour la génération de codes campagne.
- Correction de bugs mineurs d'interface utilisateur et de rendu.
- Suppression des informations de géolocalisation inutilisées.
- Suppression du bouton "ajouter une structure".
- Correction de l'affichage des comptes en attente.
- Suppression de la méthode inutilisée.
- Suppression de la page admin/sign_up.
- Correction du lien d'invitation avec structure_id.
- Correction de l'affichage du lien vers les métiers dans la restitution.
- Changement de libellé d'un bouton pour éviter un retour à la ligne.
- Correction de la vue partielle manquante restitution pdf positionnement numeratie.
- Correction de la position des éléments dans l'interface.
- Correction de l'affichage des actualités.
- Correction de l'affichage du menu déroulant.
- Ajout de commentaires et de documentation.
- Suppression de la bordure superflue.
- Correction de l'affichage des invitations en attente.
- Ajout d'effets de transition et de survol aux cartes incontournables.
- Création du composant "les incontournables".
- Suppression de la hauteur fixe et troncature de la description.
- Correction du DoubleRenderError de nouveaux_comptes_controller.
- Déplacement du menu « Opérateurs de compétences » dans le menu accompagnement.
- Correction des tests suite à la montée de version de jwt.
- Ajout de mailers/structure/invitation_structure.
- Aligne le breakpoint @media 768px sur celui du DSFR (48em).
- Permet de générer les PDF en dev.
- Ajoute les liens vers les etapes.
- Ajoute des effets de transition et de survol aux cartes incontournables.
- Crée le composant les incontournables et le place dans la vue.
- Range par ordre alphabetique les ui_kits.
- Permet aux incontournables d'etre comme avant dans le pdf.
- Reactive l'autocomplete de recherche sur les campagne prive.
- Renomme les svg correctement.
- Ajoute un test manquant lors de la génération de code campagne.
- Ne permet plus de générer des codes campagne génants.
- Corrige margin/padding suite à la suppression des utilities de bootstrap.
- Renomme les svg correctement.
- Ajoute les liens vers les etapes.
- Ajoute des effets de transition et de survol aux cartes incontournables.
- Crée le composant les incontournables et le place dans la vue.
- Range par ordre alphabetique les ui_kits.
- Permet aux incontournables d'etre comme avant dans le pdf.
- Corrige un test qui échoue aléatoirement.
- Corrige le rendu de l'index compte sur EvaPro.
- Corrige l'affichage de l'index des évaluations pour eva pro.
- Corrige le problème d'affichage sur les restitutions eva.
- Corrige les classes bootstrap des utilities qui n'ont pas été converties pour utiliser le DSFR.
