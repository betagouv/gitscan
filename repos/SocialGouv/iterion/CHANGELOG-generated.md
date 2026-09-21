## Changelog : iterion (30 derniers jours, au 20 septembre 2026)

### Résumé
Cette période a été marquée par une évolution majeure de la plateforme, notamment avec la transition vers le "DSL Profile 2", qui stabilise et renforce la syntaxe de définition des workflows. Le catalogue de bots s'est considérablement enrichi avec l'arrivée de nouveaux agents spécialisés (Revi, Billy, Senti, etc.), et l'interface de gestion (Studio) a été modernisée pour offrir un contrôle plus fin sur les ressources et les dépenses de crédits. La fiabilité globale de l'exécution, particulièrement en environnement cloud et sandbox, a été renforcée par de nombreuses optimisations de l'infrastructure et de la gestion des reprises (resume).

### Évolutions fonctionnelles

**Bots & Agents**
- Lancement de l'épic "Iterion Assistant" introduisant une nouvelle génération de bots spécialisés [#480](https://github.com/SocialGouv/iterion/issues/480).
- Mise à disposition d'un catalogue de bots basé sur des modèles (templates) standardisés pour faciliter la création [#1114](https://github.com/SocialGouv/iterion/issues/1114).
- Amélioration des capacités de revue de code par IA, incluant des détails de runs liés directement dans les commentaires de revue [#1173](https://github.com/SocialGouv/iterion/issues/1173).
- Introduction de "Senti", un agent de surveillance des vulnérabilités basé sur l'inventaire sans recours systématique aux LLM [#515](https://github.com/SocialGouv/iterion/issues/515).

**Studio & Administration**
- Refonte de l'interface d'accueil Cloud pour se concentrer sur l'orchestration [#1028](https://github.com/SocialGouv/iterion/issues/1028).
- Ajout de nouveaux écrans d'administration pour le suivi des dépenses de crédits (credential spend) et des limites d'utilisation de la plateforme [#1444](https://github.com/SocialGouv/iterion/issues/1444), [#1442](https://github.com/SocialGouv/iterion/issues/1442).
- Amélioration de la navigation organisationnelle avec un accès direct aux équipes depuis le menu admin [#1446](https://github.com/SocialGouv/iterion/issues/1446).

**DSL & Workflows**
- Migration vers le "DSL Profile 2" apportant une syntaxe plus robuste, une meilleure gestion des imports et des diagnostics de compilation plus précis [#1344](https://github.com/SocialGouv/iterion/issues/1344), [#1154](https://github.com/SocialGouv/iterion/issues/1154).
- Introduction de la validation par "dry-run" permettant de tester la validité des workflows et des variables avant l'exécution réelle [#1292](https://github.com/SocialGouv/iterion/issues/1292).

### Évolutions techniques

**Runtime & Exécution**
- Amélioration de la résilience des runs : les décisions de lancement (mode sandbox, cibles de merge) et les réponses des agents sont désormais persistées lors d'une reprise (resume) [#1490](https://github.com/SocialGouv/iterion/issues/1490).
- Renforcement de l'isolation des sandboxes et de la gestion des sous-bots (subbots) pour éviter les collisions de ressources [#1195](https://github.com/SocialGouv/iterion/issues/1195).
- Optimisation de la gestion des ressources Kubernetes, incluant la configuration des `priorityClassName` et du `node spread` pour les pods [#802](https://github.com/SocialGouv/iterion/issues/802), [#694](https://github.com/SocialGouv/iterion/issues/694).
- Amélioration de la récupération des espaces de travail (workspaces) et des checkpoints après une interruption [#988](https://github.com/SocialGouv/iterion/issues/988).

**Sécurité & Identité**
- Gestion plus granulaire des secrets et des credentials, permettant notamment à une organisation de partager ses clés LLM avec ses équipes [#1370](https://github.com/SocialGouv/iterion/issues/1370).
- Renforcement de la sécurité des API via la correction de failles CSRF [#1058](https://github.com/SocialGouv/iterion/issues/1058).
- Amélioration des processus d'audit de sécurité avec des scans profonds (deep scans) plus fiables et une meilleure remontée des résultats [#1104](https://github.com/SocialGouv/iterion/issues/1104).

**Infrastructure & CI/CD**
- Mise à jour des images de runners ARC avec support `cgo` pour une meilleure compatibilité [#981](https://github.com/SocialGouv/iterion/issues/981).
- Optimisation de la suite de tests E2E avec une exécution en parallèle pour réduire les temps de validation [#880](https://github.com/SocialGouv/iterion/issues/880).

### Autres changements

- Refonte de l'identité visuelle (branding) avec l'intégration de la mascotte "Iterion-bot" sur l'ensemble de la plateforme (icônes, logos, avatars) [#794](https://github.com/SocialGouv/iterion/issues/794).
- Mise à jour majeure de la documentation, incluant des guides sur le nouveau DSL et des bilans opérationnels [#1342](https://github.com/SocialGouv/iterion/issues/1342), [#591](https://github.com/SocialGouv/iterion/issues/591).
