## Changelog : IAssistant-Direct (30 derniers jours, au 21 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec l'introduction de la "Bulle + IA", une interface interactive permettant d'accéder directement aux fonctionnalités d'intelligence artificielle sur les sites web compatibles. Nous avons également renforcé la fiabilité des réponses dans la section "Mes collections" et assuré une compatibilité accrue avec Firefox, tout en stabilisant les processus d'authentification.

### Évolutions fonctionnelles
- **Déploiement de la "Bulle + IA"** : Mise en place de la détection automatique des sites compatibles, d'un panneau conversationnel et d'une interface popup personnalisable (opacité réglable). [#7](https://github.com/IA-Generative/IAssistant-Direct/pull/7), [#8](https://github.com/IA-Generative/IAssistant-Direct/pull/8), [#13](https://github.com/IA-Generative/IAssistant-Direct/pull/13)
- **Amélioration de "Mes collections"** : Ajout de badges pour identifier les réponses fiables, affichage de la source des assistants et présentation structurée via des plans de réponse. [#15](https://github.com/IA-Generative/IAssistant-Direct/pull/15)
- **Optimisation de l'expérience Firefox** : Amélioration du flux de connexion pour garantir une navigation fluide sur ce navigateur. [#14](https://github.com/IA-Generative/IAssistant-Direct/pull/14)

### Évolutions techniques
- **Fiabilisation de l'authentification** : Correction des pertes de session PKCE liées à l'arrêt du Service Worker et amélioration du diagnostic des erreurs de connexion Keycloak. [#10](https://github.com/IA-Generative/IAssistant-Direct/pull/10), [#11](https://github.com/IA-Generative/IAssistant-Direct/pull/11)
- **Compatibilité Firefox ESR** : Adaptation de la gestion de l'arrière-plan via `background.scripts` pour supporter les versions de Firefox ne gérant pas les Service Workers. [#6](https://github.com/IA-Generative/IAssistant-Direct/pull/6)
- **Qualité et CI/CD** : Intégration de tests de fumée (*smoke tests*) pour valider les étapes de build et de déploiement automatique.

### Autres changements
- **Documentation** : Mise à jour des guides d'architecture (onboarding) et des spécifications fonctionnelles concernant la bulle d'interface et les contrats de recherche. [#2](https://github.com/IA-Generative/IAssistant-Direct/pull/2), [#4](https://github.com/IA-Generative/IAssistant-Direct/pull/4)
- **Tests et Recettes** : Campagnes de tests intensives sur les interfaces "Mes collections" et la "Bulle" pour assurer la stabilité sur Chrome et Firefox ESR.
