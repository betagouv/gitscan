## Changelog : ci (30 derniers jours, au 13 octobre 2026)

### Résumé
Les évolutions de ce mois se concentrent sur le renforcement de la sécurité des processus d'automatisation et l'optimisation de la rapidité des constructions (builds) grâce à une meilleure gestion du cache Docker.

### Évolutions techniques
- **Optimisation des performances** : Mise en place du cache des couches d'images Docker pour accélérer les temps de construction.
- **Sécurité et stabilité des workflows** :
    - Verrouillage des versions des actions (notamment `actions/checkout` en version 7.0.1) et utilisation de digests d'images pour l'exécution de `actionlint`.
    - Sécurisation de l'authentification en désactivant la persistance des identifiants (`persist-credentials: false`) lors du checkout.
    - Mise à jour de l'outil de scan de sécurité `trivy-action` vers la version 0.36.0.

### Autres changements
- **Documentation** : Amélioration de la clarté des commentaires concernant le verrouillage des versions des actions utilisées.
