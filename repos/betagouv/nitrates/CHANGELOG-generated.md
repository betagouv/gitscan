## Changelog : nitrates (30 derniers jours, au 14 septembre 2026)

### Résumé
Ce mois-ci, nitrates a bénéficié d'une amélioration significative de son ergonomie et de son interface, notamment grâce à un alignement renforcé sur le Design System de l'État (DSFR). Le parcours utilisateur a été fluidifié par une gestion plus intelligente des questions de saisie. En parallèle, des travaux importants ont été menés sur la surveillance et la stabilité de l'infrastructure pour garantir une meilleure fiabilité du service.

### Évolutions fonctionnelles
- **Amélioration de l'interface (UI) :** Alignement des champs de dates sur les standards DSFR [#252], ajout de badges pour les rappels de période dans le volet de conditions [#487] et refonte visuelle de l'encart récapitulatif (couleurs, mise en page et espacements) [#408].
- **Optimisation de l'expérience utilisateur (UX) :** 
    - Simplification du questionnaire en sautant automatiquement les questions de sous-fertilisants lorsqu'un seul choix est disponible [#430].
    - Accès facilité aux définitions en rendant toute la surface des labels cliquable [#436].
    - Amélioration de la gestion de l'encart d'avis (affichage latéral lors de l'intention de sortie) [#435].
- **Données et contenus :** Mise à jour des référentiels réglementaires et ajustement des blocs de calcul pour les plafonds [#0d7a9fc9].
- **Corrections :** Rectification des libellés pour les questions complémentaires et correction de l'affichage des types de fertilisants dans les encarts [#408].

### Évolutions techniques
- **Observabilité et monitoring :** 
    - Mise en place d'une télémétrie continue de l'infrastructure vers Sentry [#476].
    - Ajout de sondes de surveillance sur l'environnement de staging pour mieux détecter les ralentissements.
    - Amélioration des protocoles de mesure de performance.
- **Infrastructure et Ops :** 
    - Optimisation de la configuration Gunicorn pour résoudre des problèmes de performance sur l'environnement de staging [#456].
    - Automatisation et ajustement des redémarrages nocturnes pour stabiliser l'exécution des tâches planifiées (crons).
    - Amélioration de la résilience des tâches ponctuelles (*one-offs*).
- **Sécurité :** Mise en conformité avec la RFC 9116 via l'implémentation du fichier `security.txt` [#443].
- **Tests et Analytics :** 
    - Alignement des tests de bout en bout (E2E) sur les comportements réels de l'application [#493].
    - Ajout de suivi analytique Matomo sur les champs de dates du calendrier [#252].
