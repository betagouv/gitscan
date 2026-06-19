## Changelog : transfers (30 derniers jours, au 18 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment une meilleure présentation des dates, un renforcement de la sécurité des téléchargements et la possibilité de se connecter via ProConnect sans authentification préalable. L'architecture du frontend a également été modernisée avec le passage à Vite et TanStack Router.

### Évolutions fonctionnelles
- **Téléchargements sécurisés :** Renforcement du flux de téléchargement et correction des points soulevés lors de la revue de sécurité. [#11](https://github.com/suitenumerique/transfers/issues/11)
- **Connexion ProConnect simplifiée :** Ajout d'un flux de connexion via ProConnect sans nécessiter d'authentification préalable. [#13](https://github.com/suitenumerique/transfers/issues/13)
- **Liens de téléchargement temporaires :** Implémentation de liens de téléchargement uniques qui s'auto-désactivent après le premier téléchargement complet. [#5](https://github.com/suitenumerique/transfers/issues/5)
- **Affichage des dates amélioré :** Les dates sont désormais affichées de manière plus intuitive, avec des indications relatives (ex: "il y a 2 jours") et la date complète au survol.
- **Documentation :** Ajout de documentation.

### Évolutions techniques
- **Migration Frontend :** Refonte complète du frontend avec la migration de Next.js vers Vite et TanStack Router pour une meilleure performance et une architecture plus moderne.
- **Optimisations Frontend :** Corrections suite aux retours de CodeRabbit pour améliorer la qualité du code frontend.
- **Dépendances Frontend :** Déplacement de TanStack Router vers les dépendances de développement.

### Autres changements
- Nettoyage et optimisation du code.
