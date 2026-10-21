## Changelog : playground (30 derniers jours, au 19 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la stabilisation du workflow de traduction assistée par IA et l'amélioration de la visibilité des erreurs via des notifications Slack. Le projet prépare également une transition technique majeure vers une nouvelle architecture d'agents.

### Évolutions fonctionnelles
- **Fiabilité des traductions IA** : Correction des problèmes de publication et de gestion des statuts après régénération [[#346](https://github.com/refugies-info/playground/issues/1559), [#343](https://github.com/refugies-info/playground/issues/1536), [#348](https://github.com/refugies-info/playground/issues/1430)] et amélioration de la qualité des réponses en forçant les modèles LLM [[#349](https://github.com/refugies-info/playground/issues/1562)].
- **Interface utilisateur et expérience** : Ajout de la date de publication dans les tableaux [[#335](https://github.com/refugies-info/playground/issues/1548)], amélioration de l'affichage des liens externes [[#350](https://github.com/refugies-info/playground/issues/1577)] et correction de la visibilité des contenus publiés pour les traducteurs.
- **Notifications** : Mise en place d'alertes Slack pour signaler les échecs de traduction et la fin des processus d'intégration continue (CI) [[#351](https://github.com/refugies-info/playground/issues/1483)].

### Évolutions techniques
- **Migration des agents** : Durcissement de l'interface de l'API Letta v1 en préparation de la migration [[#340](https://github.com/refugies-info/playground/issues/tec-63)] et amélioration de la traçabilité en enregistrant les modèles d'agents utilisés dans les rapports [[#342](https://github.com/refugies-info/playground/issues/tec-65)].
- **Gestion des données et traçabilité** : Intégration de l'identifiant `origin_id` dans les schémas et les webhooks [[#337](https://github.com/refugies-info/playground/issues/1549), [#330](https://github.com/refugies-info/playground/issues/tec-plan-migration-agent-sdk)] et résolution de problèmes de métadonnées manquantes dans Supabase [[#352](https://github.com/refugies-info/playground/issues/1596)].
- **Sécurité et CI/CD** : Correction d'une vulnérabilité critique sur Next.js et optimisation des workflows de revue de code.

### Autres changements
- **Documentation** : Rédaction et mise à jour approfondie de la documentation concernant le plan de migration des agents.
- **Maintenance** : Nettoyage du code (suppression de commentaires et de scripts obsolètes).
