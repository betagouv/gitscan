## Changelog : monitorfish (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions de monitorfish se concentrent sur l'amélioration de l'interface utilisateur, notamment pour les contrôles en mer et à la débarque, ainsi que sur l'ajout de nouvelles fonctionnalités liées aux groupes prioritaires de navires et aux signalements INN. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Contrôles en mer et à la débarque (e-ISR):** Modifications et corrections pour s'adapter à la version 1.3 d'e-ISR, incluant la gestion des infractions, des zones attribuées et des champs spécifiques. [#5225, #5228, #5170, #5175, #5161]
- **Groupes prioritaires:** Ajout de la description des groupes prioritaires dans les nouvelles fonctionnalités et affichage avec des icônes de ciblage. Possibilité de tester et d'utiliser les groupes prioritaires en mer. [#5231, #5215]
- **Signalements INN:** Amélioration des filtres dans la liste des signalements INN, permettant une recherche plus précise et l'ajout de filtres pour les types de signalement et l'ID du navire. Possibilité de mettre à jour les signalements directement depuis l'interface. [#5113, #5151]
- **NATINF:** Ajout des NATINF 4789 et 30013. [#5149, #5167]
- **Missions:** Ajout du type de moyen des unités de contrôles. [#5145]
- **Gestion des espèces:** Amélioration de l'affichage et de la gestion des espèces lors des contrôles, avec la possibilité de ne pas les inclure dans le relevé.
- **Préavis:** Affichage des messages manuels dans la marée du navire. [#5222]

### Évolutions techniques
- **Backend:** Mise à jour des dépendances Spring Boot (4), Security (7), Flyway (12), Ktor (3.5) et d'autres dépendances mineures. [#5146, #5148]
- **Tests:** Correction de tests flakys et ajout de tests pour les nouveaux groupes prioritaires.
- **CI/CD:** Modification du workflow CI/CD pour la gestion des source maps Sentry.
- **Architecture:** Refactorisation du code pour améliorer la maintenabilité et les performances.
- **Docker:** Ajout de la variable d'environnement `MONITORFISH_KAFKA_AIS_TOPIC` au fichier docker-compose.
- **Frontend:** Migration vers des versions plus récentes de certaines librairies frontend (uuid, TS-ESLint, styled-components, monitor-ui).

### Autres changements
- Ajout d'un README pour la génération du fichier .p12. [#5123]
- Correction de la documentation et des commentaires dans le code.
- Amélioration de l'accessibilité de certains composants de l'interface utilisateur.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout d'index pour l'import des notes de vente dans le data warehouse. [#5196]
- Correction du parser des notes de vente FLUX. [#5173]
- Ajout du champ `is_under_jdp` à la table `analytics_missions`. [#5162]
- Correction de la gestion des dates dans les requêtes natives Hibernate.
