## Changelog : hyyypertool (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à la gestion des équipes et des accès, ainsi qu'à la sécurité et la robustesse de l'application. Des corrections de bugs ont été implémentées pour améliorer l'expérience utilisateur, notamment concernant la gestion des modérations et des domaines. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la performance de l'outil.

### Évolutions fonctionnelles
- Ajout de la gestion des équipes avec contrôle d'accès basé sur les rôles [#1477](https://github.com/proconnect-gouv/hyyypertool/pull/1477)
- Automatisation de la vérification de domaine lors de l'ajout de domaines autorisés [#1433](https://github.com/proconnect-gouv/hyyypertool/issues/1433)
- Amélioration du filtre de modération avec la population depuis la base de données et les variables d'environnement.
- Ajout de l'affichage de la tranche d'effectifs de l'unité légale dans le composant organisation.
- Amélioration de l'accessibilité des tableaux avec des liens d'ancrage appropriés et une navigation au clavier.
- Correction d'un bug empêchant la réinitialisation de la page lors de la recherche dans des listes paginées.
- Correction d'un bug lié à la mise à jour des membres liés lors de la modification du domaine email.
- Correction d'un bug empêchant l'affichage correct du tableau lors d'un rafraîchissement.

### Évolutions techniques
- Refactorisation de la configuration et de la structure des middlewares.
- Suppression de l'intégration Zammad et remplacement par Crisp pour la gestion des tickets de modération.
- Suppression de la sécurité au niveau des lignes (Row-Level Security) dans Hyperbase.
- Simplification de la fonction `set_hyyyper_pg` pour accepter une instance Drizzle pré-créée.
- Mise en place d'une authentification duale via les variables d'environnement et les utilisateurs Hyperbase.
- Suppression du fichier `.eslintrc`.
- Intégration de Sentry pour l'initiation précoce et l'ajout de profiling et du SDK navigateur.
- Mise à jour de la couche d'abstraction de la base de données Hyperbase.

### Autres changements
- Mise à jour des dépendances : hono, preact, sentry, tailwindcss, etc. (plusieurs commits dependabot)
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de code legacy lié à l'intégration Zammad.
- Amélioration de la gestion des erreurs et ajout de détails dans les notifications.
- Simplification du filtre de modération.
- Suppression de la fonction force join organization.
- Mise à jour de la documentation.
