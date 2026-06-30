## Changelog : eva-serveur (30 derniers jours, au 28 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur les pages de connexion et de création de compte, ainsi que sur la gestion des évaluations Evapro. Des corrections de bugs ont été apportées pour stabiliser l'application et améliorer la gestion des données, en particulier lors de l'importation et de la restitution des évaluations. Des refactorings ont également été réalisés pour moderniser le code et préparer l'application à de futures évolutions.

### Évolutions fonctionnelles
- Ajout de la navigation vers la liste des campagnes depuis un compte utilisateur.
- Amélioration de l'accessibilité des pages de connexion et de création de compte (boutons actifs par défaut, hints clairs).
- Création de nouveaux modèles `EvaluationEva` et `EvaluationEvapro` pour une meilleure gestion des évaluations.
- Ajout de nouveaux accès démos depuis l'accueil.
- Correction de l'affichage de la durée estimée d'une évaluation Evapro.
- Correction du crash lors de la restitution d'une évaluation de campagne sans `parcourtype`.
- Correction du comportement de l'accordéon de la numératie (suppression du JS custom).
- Amélioration de la gestion des réponses multiples à la même question dans les évaluations Evapro (prise de la dernière réponse).
- Correction d'un crash lors de l'importation d'un grand nombre d'erreurs.
- Possibilité d'importer des questions avec des noms techniques de choix existants.
- Ajout de profils aberrants pour la comparaison.
- Ajout d'indicateurs de coût actualisés.
- Actualisation des conseils des bilans Evapro.

### Évolutions techniques
- Mise à jour de plusieurs dépendances, dont Puma (7.2), image_processing (de 1.14.0 à 2.0.2, nécessitant l'installation de ruby-vips) et js-yaml (de 4.1.1 à 4.2.0).
- Refactoring de la configuration d'erd pour utiliser Mermaid au lieu de PNG.
- Simplification de la map des malus de pourcentage de risque.
- Suppression de code commun redondant entre `input_component` et `password_input_component`.
- Création d'un nouveau composant `PasswordInputComponent` conforme au DSFR.
- Utilisation de lettres en majuscule pour les paliers.
- Introduction d'un layout `ui_kit` pour une meilleure cohérence visuelle.
- Suppression du composant `impact_stepper` non utilisé.
- Généralisation de la suppression des réponses lors de l'import.
- Simplification de `cout_presenter`.
- Suppression des exemples de stratégies de contournement obsolètes.
- Correction d'une race condition à la connexion Pro-Connect.
- Réactivation de la vérification du token d'authenticité.
- Retour à la configuration par défaut pour CodeQL.

### Autres changements
- Amélioration de la documentation des indicateurs de risque.
- Ajout d'opacité pour les EvaProScore.
- Correction de l'affichage du hint pour le mot de passe pour les superadmins.
- Correction du crash lors de la tentative de définition d'un mot de passe invalide.
- Correction du calcul du score de stratégie (basé sur les données pour le score numérique).
- Ajout de traductions et formatage du SIRET dans le choix de structure.
- Suppression des exemples de UI Kit.
- Correction du style du bouton d'ajout de réponse.
- Correction du style du badge aberrant.
- Correction de la structure de la page de login pour l'accessibilité.
- Migration de la page de démo d'eva vers le nouveau layout.
- Reprise des textes de l'écran de choix de l'usage.
- Rétablissement de la marge sous les titres h3 de la numératie.
- Actualisation des stanines des impacts, de l'analyse de risque et des coûts.
- Extraction des chaînes de `impact_couts` dans le fichier de traduction.
- Correction d'un bug lié à la restitution d'une évaluation Evapro avec un score total supérieur à 167.
- Correction d'un bug empêchant la suppression des choix retirés d'une question lors de l'import.
