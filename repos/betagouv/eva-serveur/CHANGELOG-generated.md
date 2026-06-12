## Changelog : eva-serveur (30 derniers jours, au 11 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment une migration vers le nouveau layout DSFR, des corrections d'accessibilité et des ajustements visuels. Des optimisations ont été apportées à la gestion des structures et des utilisateurs, ainsi que des corrections de bugs et des mises à jour de dépendances pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Possibilité de fermer la modale de validation en attente en cliquant sur le fond.
- Affichage et filtrage du SIRET pour toutes les structures.
- Ajout d'accès démos depuis l'accueil.
- Ajout de liens officiels pour les compétences transversales.
- Restauration des fonctions d'autocomplétion pour la recherche de compte.
- Réactivation de l'autocomplete de recherche sur les campagnes privées.
- Possibilité de générer les PDF en environnement de développement.
- Ajout d'une colonne SIRET à la table des comptes.
- Suppression des choix retirés d'une question lors de l'import de questions QCM.
- Ajout du profil aberrant pour la comparaison.
- Ajout d'indicateurs de coût actualisés.
- Ajout de conseils actualisés pour les bilans Evapro.
- Ajout de nouvelles permissions pour CodeQL.

### Évolutions techniques
- Migration de la page de démo d'eva vers le nouveau layout DSFR.
- Refonte de l'interface utilisateur avec le DSFR (Design System Fr).
- Suppression de l'ancienne vague de fond.
- Correction de la structure de la page de login pour l'accessibilité.
- Mise à jour de la dépendance `jwt` vers la version 3.2.0.
- Mise à jour de la dépendance `devise` vers la version 5.0.4.
- Mise à jour de la dépendance `fast-uri` vers la version 3.1.2.
- Mise à jour de la dépendance `image_processing` vers la version 2.0.2 (nécessite l'installation de ruby-vips).
- Mise à jour de la dépendance `Puma` vers la version 7.2.
- Simplification du code `cout_presenter`.
- Suppression du composant `impact_stepper` non utilisé.
- Généralisation de la suppression des réponses à l'import.
- Suppression de code inutilisé et nettoyage du code.
- Utilisation des lettres en majuscule pour les paliers.
- Correction d'un `DoubleRenderError` dans le contrôleur `nouveaux_comptes`.
- Suppression des utilities Bootstrap.
- Correction de problèmes de rendu sur EvaPro.
- Refactorisation et correction des ouvertures de modales.

### Autres changements
- Documentation améliorée des indicateurs de risque.
- Ajout d'opacité pour les EvaProScore.
- Ajout de traductions et formatage du SIRET dans le choix de structure.
- Suppression d'exemples de stratégie de contournement obsolètes.
- Correction du calcul de `score_strategie`.
- Extraction des chaînes de caractères liées aux coûts dans les fichiers de traduction.
- Ajout d'un composant Metabase iframe pour les structures.
- Ajout de tests pour la génération de codes campagne.
- Correction de tests suite à la mise à jour de `jwt`.
- Suppression du bouton copier/coller dans la modal invitation des structures Opco et Administrative.
- Correction de l'affichage des actualités.
- Correction de l'affichage de l'index des évaluations pour EvaPro.
- Ajout de commentaires et documentation pour clarifier le code.
- Correction de problèmes de style et d'affichage.
- Ajout de tests unitaires et d'intégration.
- Correction de bugs mineurs et améliorations de la performance.
- Suppression de fichiers CSS inutilisés.
- Ajout de liens vers les étapes du parcours utilisateur.
- Ajout d'effets de transition et de survol aux cartes incontournables.
- Création du composant "les incontournables".
- Suppression de la hauteur fixe et troncature de la description.
