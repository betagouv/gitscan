## Changelog : srdt (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de la précision des réponses juridiques, notamment grâce à une meilleure intégration de la jurisprudence dans le système d'intelligence artificielle. L'expérience utilisateur a également été enrichie par une meilleure visibilité des sources et des outils de manipulation des réponses plus intuitifs.

### Évolutions fonctionnelles
- **Amélioration de la visibilité des sources** : les sources sont désormais affichées dans un panneau latéral ([#409](https://github.com/SocialGouv/srdt/issues/409)) et incluent des détails précis comme le numéro de pourvoi et la date pour la jurisprudence ([#419](https://github.com/SocialGouv/srdt/issues/419)).
- **Précision du contexte** : la convention collective est désormais systématiquement précisée après la première réponse ([#424](https://github.com/SocialGouv/srdt/issues/424)).
- **Nouvelles interactions utilisateur** : possibilité de copier une section spécifique d'une réponse plutôt que l'intégralité ([#426](https://github.com/SocialGouv/srdt/issues/426)).
- **Optimisation de l'affichage** : les titres de jurisprudence incluent désormais les références de la décision et les résultats sont reclassés (rerank) pour une meilleure pertinence.
- **Nettoyage de l'interface** : suppression du lien de support de l'en-tête ([#405](https://github.com/SocialGouv/srdt/issues/405)).

### Évolutions techniques
- **Optimisation de l'IA et du RAG** : intégration de la jurisprudence dans le processus RAG, ajustement des prompts pour renforcer la rigueur des réponses et fixation de la température à 0.3 pour les appels Mistral afin de stabiliser la génération.
- **Refonte et évolutions API** : restructuration de l'architecture de l'API, ajout de la recherche dans les accords complets ([#399](https://github.com/SocialGouv/srdt/issues/399)) et mise à jour de l'intégration Judilibre ([#411](https://github.com/SocialGouv/srdt/issues/411)).
- **Performance et gestion du contexte** : limitation de l'historique de conversation à 12 entrées pour optimiser la gestion de la mémoire de l'IA ([#417](https://github.com/SocialGouv/srdt/issues/417), [#423](https://github.com/SocialGouv/srdt/issues/423)).
- **Sécurité et maintenance** : amélioration des processus d'anonymisation et des logs, mise à jour des domaines pour Proconnect ([#422](https://github.com/SocialGouv/srdt/issues/422)) et correction de bugs d'affichage liés à `react-markdown` ([#425](https://github.com/SocialGouv/srdt/issues/425)).
