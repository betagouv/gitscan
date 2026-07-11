## Changelog : eva-serveur (30 derniers jours, au 9 juillet 2026)

### Résumé
Les dernières évolutions d'eva-serveur se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur les formulaires d'évaluation et la gestion des comptes utilisateurs. Des corrections de bugs ont été apportées pour stabiliser l'application et améliorer sa robustesse, en particulier lors de l'importation de données et de la restitution des évaluations Evapro. Des améliorations techniques ont également été réalisées pour moderniser l'infrastructure et optimiser les performances.

### Évolutions fonctionnelles

- Correction du formulaire de modification d'une évaluation [#39044c4](https://github.com/betagouv/eva-serveur/commit/39044c4)
- Suppression de la proposition de rejoindre des structures administratives lors de l'inscription [#b123c23](https://github.com/betagouv/eva-serveur/commit/b123c23)
- Ajout de la navigation vers la liste des campagnes depuis un compte utilisateur [#d5c9ab6](https://github.com/betagouv/eva-serveur/commit/d5c9ab6)
- Amélioration de la gestion des réponses multiples pour les évaluations Evapro : sélection de la dernière réponse [#542f436](https://github.com/betagouv/eva-serveur/commit/542f436)
- Correction d'un crash lors de la restitution d'une évaluation de campagne sans parcourtype [#2328652](https://github.com/betagouv/eva-serveur/commit/2328652)
- Correction de l'affichage du hint pour le mot de passe pour les superadmins [#8184777](https://github.com/betagouv/eva-serveur/commit/8184777)
- Correction du crash lors de la définition d'un mot de passe invalide [#75a5c08](https://github.com/betagouv/eva-serveur/commit/75a5c08)
- Ajout de nouveaux accès démos depuis l'accueil [#1a2e18e](https://github.com/betagouv/eva-serveur/commit/1a2e18e)
- Ajout du profil "aberrant" pour la comparaison [#7d1fc5f](https://github.com/betagouv/eva-serveur/commit/7d1fc5f)
- Correction de la durée estimée d'une évaluation Evapro [#bf30d45](https://github.com/betagouv/eva-serveur/commit/bf30d45)

### Évolutions techniques

- Mise à jour de Ruby et des dépendances, incluant Puma 7.2 et image_processing [#4d8d2b8](https://github.com/betagouv/eva-serveur/commit/4d8d2b8)
- Génération du schéma de la base de données au format Mermaid pour une meilleure lisibilité [#58be733](https://github.com/betagouv/eva-serveur/commit/58be733)
- Refactoring du code commun entre `input_component` et `password_input_component` [#045814c](https://github.com/betagouv/eva-serveur/commit/045814c)
- Création du composant `PasswordInputComponent` conforme au DSFR [#194e21a](https://github.com/betagouv/eva-serveur/commit/194e21a)
- Suppression de l'ancienne vague de fond et migration de la page de démo vers le nouveau layout [#cf1ab9f](https://github.com/betagouv/eva-serveur/commit/cf1ab9f)
- Correction d'une race condition à la connexion Pro-Connect [#5d8c9ec](https://github.com/betagouv/eva-serveur/commit/5d8c9ec)
- Réactivation de la vérification du token d'authenticité [#c9c8eaa](https://github.com/betagouv/eva-serveur/commit/c9c8eaa)
- Simplification de la map des malus de pourcentage de risque [#dd4b64f](https://github.com/betagouv/eva-serveur/commit/dd4b64f)
- Correction d'un problème d'affichage du hint lors du changement de mot de passe pour les comptes non Anci [#124f7ce](https://github.com/betagouv/eva-serveur/commit/124f7ce)

### Autres changements

- Amélioration de la documentation et des tests pour l'indicateur de risque [#9bd7b00](https://github.com/betagouv/eva-serveur/commit/9bd7b00)
- Ajout d'opacité pour les EvaProScore [#00249f7](https://github.com/betagouv/eva-serveur/commit/00249f7)
- Correction de la structure de la page de login pour l'accessibilité [#9eec9ae](https://github.com/betagouv/eva-serveur/commit/9eec9ae)
- Rétablissement des textes de l'écran de choix d'usage [#3012240](https://github.com/betagouv/eva-serveur/commit/3012240)
- Rétablissement de la marge sous les titres h3 de la numératie [#1a2e18e](https://github.com/betagouv/eva-serveur/commit/1a2e18e)
- Correction d'un crash lors de l'importation avec des erreurs [#b18d7a8](https://github.com/betagouv/eva-serveur/commit/b18d7a8)
- Permettre l'import de questions avec des noms techniques de choix existants [#5aeb734](https://github.com/betagouv/eva-serveur/commit/5aeb734)
- Suppression du JS custom qui empêchait l'accordéon numératie de s'ouvrir [#7dd8952](https://github.com/betagouv/eva-serveur/commit/7dd8952)
- Mise à jour de la configuration d'erd [#8839b7e](https://github.com/betagouv/eva-serveur/commit/8839b7e)
- Correction d'un bug d'affichage du score total d'une évaluation Evapro [#f53b8e2](https://github.com/betagouv/eva-serveur/commit/f53b8e2)
- Ajout des permissions pour CodeQL [#b73dbca](https://github.com/betagouv/eva-serveur/commit/b73dbca)
- Retour à la configuration par défaut pour CodeQL [#1240227](https://github.com/betagouv/eva-serveur/commit/1240227)
- Suppression d'un warning sur un nom de vue sans html.erb [#0a3563e](https://github.com/betagouv/eva-serveur/commit/0a3563e)
- Création des models EvaluationEva et EvaluationEvapro [#3bbc730](https://github.com/betagouv/eva-serveur/commit/3bbc730)
- Le bouton de validation de création de compte et le bouton de reset password sont actifs par défaut [#98af57e](https://github.com/betagouv/eva-serveur/commit/98af57e) et [#3cdca00](https://github.com/betagouv/eva-serveur/commit/3cdca00)
