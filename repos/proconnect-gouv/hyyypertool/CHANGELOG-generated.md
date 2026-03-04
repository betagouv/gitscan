## Changelog : hyyypertool (30 derniers jours)

### Résumé
Les dernières mises à jour de Hyyypertool se concentrent sur la correction de bugs, l'amélioration de l'expérience utilisateur et l'optimisation des processus de modération. Des améliorations ont été apportées à la gestion des notifications, au filtrage des données, à la vérification des domaines et à la gestion des statuts de modération. Des refactorings ont également été effectués pour améliorer la maintenance et la performance du code.

### Évolutions fonctionnelles
- Les notifications de modération sont désormais envoyées via Crisp, incluant l'identité de l'opérateur, permettant un suivi plus précis des actions.
- La vérification automatique des domaines est désormais disponible lors de l'ajout de domaines autorisés.
- Amélioration de l'accessibilité du tableau des modérations avec des liens d'ancrage et une navigation au clavier.
- Ajout d'un lien vers EHPAD dans les actions d'investigation.
- Simplification du filtre de modérations.
- Refactorisation du sélecteur de membres et de domaines en un composant d'île unifié.
- Ajout de détails d'erreur dans les notifications avec une section repliable.
- Correction du comportement du filtre "hide prefix" qui cachait des informations.
- Correction du statut des modérations lors du retraitement, qui passe désormais à "reopened".
- Correction d'un bug empêchant la mise à jour des membres liés lors du changement de type de vérification d'un domaine.
- Correction d'un bug sur la table des domaines qui disparaissait lors du rafraîchissement.

### Évolutions techniques
- Suppression de l'intégration Zammad.
- Suppression du module `@~/core`.
- Refactoring de l'envoi de notifications de modération via Crisp.
- Mise à jour de plusieurs dépendances (voir section "Autres changements").
- Amélioration de la gestion des erreurs et des types de vérification.
- Mise en place de tests E2E pour la validation de membres externes avec notification et domaine.
- Utilisation de `fast-check` pour une couverture de tests plus large.
- Suppression de code legacy lié à la jointure forcée d'organisations.
- Correction de problèmes de permissions et de comportement des workflows de deforestation.

### Autres changements
- Mises à jour de dépendances :
    - `preact-render-to-string`
    - `@proconnect-gouv/proconnect.api_entreprise`
    - `tailwind-merge`
    - `@happy-dom/global-registrator`
    - `preact`
    - `openid-client`
    - `dotenv`
    - `@proconnect-gouv/proconnect.identite`
    - `@proconnect-gouv/proconnect.identite.database`
    - `pg`
    - `@types/bun`
    - `hono`
    - `hono-sessions`
    - `oxc-parser`
    - `@preact/signals`
    - `@preact/signals-core`
    - `cypress-io/github-action`
- Mise à jour de la configuration Tailwind.
- Ajout d'une politique de sécurité et de directives de signalement.
- Formatage des fichiers Gherkin avec Prettier.
- Correction de la version de Node utilisée pour l'environnement de build.
- Amélioration de la robustesse des tests E2E.
- Ajout de notes de publication pour la correction du type de vérification.
