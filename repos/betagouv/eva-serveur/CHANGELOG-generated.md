## Changelog : eva-serveur (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur les formulaires d'évaluation et de gestion des comptes, ainsi que sur la correction de bugs impactant la stabilité et la restitution des données. Des améliorations techniques ont également été apportées pour faciliter la maintenance et l'évolution du code.

### Évolutions fonctionnelles
- Correction du formulaire de modification d'une évaluation [#39044c4](https://github.com/betagouv/eva-serveur/commit/39044c4).
- Lors de l'inscription, il n'est plus proposé de rejoindre des structures administratives [#b123c23](https://github.com/betagouv/eva-serveur/commit/b123c23).
- Ajout de la navigation depuis un compte utilisateur vers la liste de ses campagnes [#d5c9ab6](https://github.com/betagouv/eva-serveur/commit/d5c9ab6).
- Correction de l'affichage du hint pour le mot de passe pour les super-admins [#8184777](https://github.com/betagouv/eva-serveur/commit/8184777).
- Correction du crash lors de la tentative de définition d'un mot de passe invalide [#75a5c08](https://github.com/betagouv/eva-serveur/commit/75a5c08).
- Correction de la durée estimée d'une évaluation Evapro [#bf30d45](https://github.com/betagouv/eva-serveur/commit/bf30d45).
- Gestion améliorée des réponses multiples à la même question dans les évaluations Evapro [#542f436](https://github.com/betagouv/eva-serveur/commit/542f436).
- Correction du crash lors de la restitution d'une évaluation de campagne sans parcourtype [#2328652](https://github.com/betagouv/eva-serveur/commit/2328652).
- Amélioration de l'accessibilité des boutons de création de compte et de réinitialisation du mot de passe (actifs par défaut) [#98af57e](https://github.com/betagouv/eva-serveur/commit/98af57e), [#7ed07c1](https://github.com/betagouv/eva-serveur/commit/7ed07c1), [#3cdca00](https://github.com/betagouv/eva-serveur/commit/3cdca00).
- Création d'un nouveau composant `PasswordInputComponent` conforme au DSFR [#194e21a](https://github.com/betagouv/eva-serveur/commit/194e21a).
- Correction du hint lors du changement de mot de passe pour les comptes non Anciens [#124f7ce](https://github.com/betagouv/eva-serveur/commit/124f7ce).

### Évolutions techniques
- Correction d'une race condition lors de la connexion via Pro-Connect [#5d8c9ec](https://github.com/betagouv/eva-serveur/commit/5d8c9ec).
- Génération du schéma de la base de données au format Mermaid (plus lisible) au lieu de PNG [#58be733](https://github.com/betagouv/eva-serveur/commit/58be733).
- Refactoring du code commun entre `input_component` et `password_input_component` [#045814c](https://github.com/betagouv/eva-serveur/commit/045814c).
- Suppression du JavaScript custom qui empêchait l'accordéon de la section numératie de s'ouvrir [#7dd8952](https://github.com/betagouv/eva-serveur/commit/7dd8952).
- Correction d'un bug lié à la restitution d'une Evaluation Evapro avec un score total supérieur à 167 [#f53b8e2](https://github.com/betagouv/eva-serveur/commit/f53b8e2).
- Simplification de la logique de mapping des malus de pourcentage de risque [#f3b2d35](https://github.com/betagouv/eva-serveur/commit/f3b2d35).
- Suppression des cas de synthese[:pourcentage_risque] utilisant un symbole [#dd4b64f](https://github.com/betagouv/eva-serveur/commit/dd4b64f).
- Mise à jour de la configuration CodeQL pour revenir à la configuration par défaut [#1240227](https://github.com/betagouv/eva-serveur/commit/1240227).
- Correction suite à la mise à jour de view-component [#646d83d](https://github.com/betagouv/eva-serveur/commit/646d83d).
- Actualisation des dépendances [#d6ec975](https://github.com/betagouv/eva-serveur/commit/d6ec975).
- Correction d'un crash lors de l'importation avec trop d'erreurs [#b18d7a8](https://github.com/betagouv/eva-serveur/commit/b18d7a8).
- Permet d'importer des questions avec des `nom_technique` de choix existant sur d'autres questions [#5aeb734](https://github.com/betagouv/eva-serveur/commit/5aeb734).

### Autres changements
- Actualisation de la configuration d'erd [#8839b7e](https://github.com/betagouv/eva-serveur/commit/8839b7e).
- Création des modèles `EvaluationEva` et `EvaluationEvapro` [#3bbc730](https://github.com/betagouv/eva-serveur/commit/3bbc730).
- Suppression d'un warning sur un nom de vue sans fichier `.erb` [#0a3563e](https://github.com/betagouv/eva-serveur/commit/0a3563e).
- Reactivation de la vérification du token d'authenticité [#c9c8eaa](https://github.com/betagouv/eva-serveur/commit/c9c8eaa).
