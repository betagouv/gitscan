## Changelog : territoires-en-transitions (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment une refonte de l'affichage des plans et des axes, avec une nouvelle gestion des sous-actions. De nombreuses corrections de bugs et optimisations de performance ont également été implémentées, ainsi que des améliorations de la sécurité et de la gestion des notifications.

### Évolutions fonctionnelles
- Ajout de la possibilité de taguer les plans. (#9817db5)
- Ajout de la gestion des préférences utilisateur, incluant la possibilité de désactiver les notifications d'affectation. (#cfb7699, #b9e0418)
- Refonte de l'affichage des plans avec une nouvelle arborescence et une gestion améliorée des axes et des sous-actions. (#385ae87, #120b65d)
- Ajout de la possibilité de déplacer les fiches dans l'arborescence du plan. (#1d8e0f2)
- Ajout d'un bouton pour ouvrir/fermer tous les axes/sous-axes. (#da66be6)
- Amélioration de la gestion des indicateurs liés aux axes. (#6866ac0)
- Ajout de la possibilité d'ajouter une description aux axes. (#1e04138)
- Ajout de la fonctionnalité de déplacement des axes. (#179ea91)
- Intégration de l'information COT (Code des Territoires) pour les collectivités et les informations utilisateur. (#ff525e8)
- Suppression du feature flag de génération de rapports, la fonctionnalité est maintenant activée par défaut. (#6f40d1b)
- Amélioration de l'affichage des indicateurs dans le détail d'un plan. (#df37e39)
- Ajout de la gestion des budgets agrégés dans le header du plan. (#1a95013)
- Ajout de la possibilité de masquer des colonnes dans le tableau des sous-actions. (#802a2da)
- Ajout d'une modale pour la suppression des sous-actions. (#641685b)

### Évolutions techniques
- Migration vers un nouveau système de rôles et permissions pour une gestion plus fine des accès. (#90420cc)
- Refactor de l'import de plan pour améliorer la performance et la robustesse. (#973e729)
- Utilisation de tRPC pour la sauvegarde des actions statuts et des commentaires dans les référentiels. (#a218361, #f06cf09)
- Suppression de l'utilisation de `luxon` au profit de librairies plus performantes. (#c1dec51, #87d7422)
- Mise à jour de Next.js pour corriger des vulnérabilités liées aux Server Side Components (RSC). (#c08fd38)
- Refonte de la feature d'import de plan. (#7ec00ab)
- Suppression de drizzle-zod. (#2e8d683)
- Migration des charts Nivo vers Echarts pour de meilleures performances et fonctionnalités. (#d3b47c4, #5bb462f)
- Activation de Turbopack pour l'optimisation des builds en développement et en production. (#d40c948, #6ae6e50)
- Amélioration de la gestion des erreurs et ajout de logs avec correlation ID. (#3ca7b83)
- Utilisation de Sentry pour la gestion des erreurs en production. (#95018da)
- Suppression de Datadog Logs. (#4f6a2b5)
- Amélioration de la gestion des permissions pour l'accès aux données. (#83e592d)

### Autres changements
- Correction de plusieurs bugs mineurs liés à l'interface utilisateur et à la gestion des données.
- Amélioration de la documentation et des tests.
- Mise à jour des dépendances.
- Amélioration des messages de notification "toast". (#97202e3)
- Ajout de tests e2e pour les nouvelles fonctionnalités.
- Correction de problèmes de linting. (#0190f9c)
- Suppression de code inutilisé.
- Amélioration de la performance de certaines requêtes. (#6c25968)
- Correction de problèmes de typage.
- Ajustement de la taille des boutons et des libellés.
- Suppression du CSS DSFR et remplacement par des composants du design system. (#9421394)
- Ajout de la fonte Marianne. (#87fa8b4)
- Correction de l'affichage des liens. (#f349379)
- Amélioration de la gestion des erreurs lors de l'import de données. (#79861f5)
- Correction de coquilles et amélioration de la clarté des messages. (#60054e5, #0ea2709)
