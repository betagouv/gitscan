## Changelog : eva-serveur (30 derniers jours, au 18 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment sur les pages de connexion et de création de compte, avec une attention particulière à l'accessibilité. Des corrections de bugs ont été apportées pour améliorer la stabilité de l'application, en particulier lors de la restitution des évaluations et de la gestion des comptes utilisateurs. Des optimisations et des refactorings ont également été réalisés pour améliorer la maintenabilité et la performance du code.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité des boutons de validation de création de compte et de réinitialisation du mot de passe.
- Ajout de la navigation vers la liste des campagnes depuis un compte utilisateur.
- Possibilité de fermer la modale de validation en attente en cliquant sur le fond.
- Ajout de nouveaux accès démos depuis l'accueil.
- Restauration des fonctions d'autocomplétion pour la recherche de compte et des campagnes privées.
- Ajout des liens vers les étapes dans les évaluations.
- Ajout d'un composant pour afficher les données Metabase pour les structures.
- Possibilité de supprimer les choix retirés d'une question lors de l'import de questions QCM.
- Ajout des URL officielles pour les compétences transversales.
- Ajout du profil aberrant pour la comparaison des données.

### Évolutions techniques
- Refactoring du code pour utiliser le nouveau layout UI Kit et les composants DSFR.
- Simplification de la logique de calcul des scores et des pourcentages de risque.
- Migration de la configuration d'Erd vers Mermaid pour une meilleure lisibilité.
- Mise à jour des dépendances, incluant Puma en version 7.2 et jwt en version 3.2.0.
- Suppression du code JavaScript custom qui empêchait l'accordéon de la numératie de s'ouvrir.
- Suppression de code inutilisé et simplification de certaines parties du code.
- Correction de race condition à la connexion Pro-Connect.
- Génération du schéma au format Mermaid plutôt que PNG.
- Suppression de l'ancienne vague de fond.
- Suppression du composant `impact_stepper` non utilisé.
- Utilisation des lettres en majuscule pour les paliers.
- Correction d'un `DoubleRenderError` dans le contrôleur `nouveaux_comptes`.
- Déplacement du menu "Opérateurs de compétences" dans le menu "accompagnement".
- Ajout d'une colonne Siret à la table des comptes.

### Autres changements
- Documentation améliorée des indicateurs de risque.
- Mise à jour des textes de l'écran de choix d'usage et des conseils des bilans Evapro.
- Actualisation des indicateurs de coût.
- Ajout de tests pour la génération de codes campagne.
- Suppression des exemples de stratégie de contournement qui ne tenaient pas sur la page.
- Correction du style du bouton d'ajout de réponse.
- Suppression des informations concernant la géoloc qui ne sont plus utilisées.
- Correction de l'affichage du hint pour le mot de passe pour les superadmins.
- Correction du crash lors de la tentative de définition d'un mot de passe invalide.
- Correction de la restitution d'une évaluation Evapro avec un score total supérieur à 167.
- Correction du crash d'une restitution d'une évaluation de campagne sans parcourtype.
- Correction du hint lors du changement de mot de passe pour les comptes non Anci.
- Ajout d'un composant `PasswordInputComponent` conforme au DSFR.
- Correction de la structure de la page de login pour l'accessibilité.
- Migration de la page de démo d'Eva vers le nouveau layout.
- Ajout d'opacité pour les EvaProScore.
- Ajout des permissions pour CodeQL.
- Suppression de la méthode inutilisée.
- Correction des marges/padding suite à la suppression des utilities de bootstrap.
- Renommage correct des SVG.
- Suppression de l'ancienne méthode d'initialisation de CopierLienInvitation.
- Correction d'un bug lié à la suppression des réponses lors de l'import.
- Correction d'un bug lié à la gestion des structures après la fin de l'embarquement.
- Ajout de la possibilité de générer les PDF en mode développement.
- Correction de l'affichage du lien vers les métiers dans la restitution.
- Correction du libellé d'un bouton pour éviter un retour à la ligne.
- Ajout de la documentation pour la variable d'environnement du tableau Metabase des OPCO.
- Suppression des classes CSS inutilisées.
- Ajout d'effets de transition et de survol aux cartes incontournables.
- Création du composant "les incontournables" et placement dans la vue.
- Organisation des UI Kits par ordre alphabétique.
- Permettre aux incontournables d'être comme avant dans le PDF.
