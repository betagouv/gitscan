## Changelog : eva-serveur (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la restitution des évaluations Evapro et de la création de compte. Des corrections de bugs ont été apportées pour assurer la stabilité de l'application, en particulier lors de l'import de données et de la gestion des erreurs. Des améliorations techniques ont également été réalisées pour moderniser le code et l'infrastructure.

### Évolutions fonctionnelles
- Ajout de la navigation vers la liste des campagnes depuis un compte utilisateur.
- Amélioration de la restitution des évaluations Evapro, notamment pour la gestion des scores et des réponses multiples.
- Correction de l'affichage de la durée estimée d'une évaluation Evapro.
- Amélioration de l'expérience de création de compte : correction des indications pour le mot de passe, activation par défaut des boutons de validation et de réinitialisation du mot de passe, et intégration d'un nouveau composant de saisie de mot de passe conforme au DSFR.
- Ajout d'accès démos depuis l'accueil.
- Ajout du profil aberrant pour la comparaison des évaluations.
- Correction de l'affichage des indicateurs de coût et actualisation des conseils pour les bilans Evapro.
- Correction du calcul du score de stratégie.
- Ajout des URL officielles pour les compétences transversales.
- Correction de l'import de questions avec des noms techniques de choix existants.
- Possibilité de supprimer les réponses lors de l'import de questions QCM.

### Évolutions techniques
- Mise à jour des dépendances, incluant Puma en version 7.2 et image_processing en version 2.0.2 (nécessitant l'installation de ruby-vips).
- Refonte des cartes de choix d'usage avec des composants DSFR.
- Génération du schéma de la base de données au format Mermaid pour une meilleure lisibilité.
- Simplification de la logique de calcul des coûts et des risques.
- Suppression de code obsolète et simplification de certaines parties du code.
- Utilisation d'un layout UI Kit pour une meilleure cohérence visuelle.
- Suppression d'un composant impact_stepper non utilisé.
- Correction d'une race condition à la connexion Pro-Connect.
- Réactivation de la vérification du token d'authenticité.
- Ajout des permissions pour CodeQL.
- Correction d'un crash lors de l'import de données en cas d'erreurs multiples.
- Correction d'un crash lors de la restitution d'une évaluation de campagne sans parcourtype.

### Autres changements
- Amélioration de la documentation des indicateurs de risque.
- Correction de l'opacité des EvaProScore.
- Suppression des exemples de stratégies de contournement obsolètes.
- Correction de la structure de la page de login pour l'accessibilité.
- Migration de la page de démonstration d'Eva vers le nouveau layout.
- Reprise des textes de l'écran de choix d'usage.
- Correction du style du bouton d'ajout de réponse.
- Correction de bugs mineurs d'affichage et de style.
- Ajout de traductions et formatage du SIRET dans le choix de la structure.
- Correction d'une vue partielle manquante lors de la restitution PDF de la positionnement numératie.
- Correction d'un problème d'affichage du hint pour le mot de passe pour les superadmins.
- Correction d'un crash lors de la tentative de définition d'un mot de passe invalide.
- Correction de la restitution d'une évaluation Evapro avec un score total supérieur à 167.
- Simplification de la map des malus de pourcentage de risque.
- Suppression des cas de synthèse avec un symbole pour le pourcentage de risque.
- Correction d'un bug lié à l'accordéon de la numératie.
- Changement de la couleur d'un badge aberrant.
- Actualisation des indicateurs de coût.
- Actualisation des conseils des bilans Evapro.
- Actualisation des stanines des impacts, de l'analyse de risque et des coûts.
- Correction d'un bug lié à la gestion du type de structure pour Evapro.
