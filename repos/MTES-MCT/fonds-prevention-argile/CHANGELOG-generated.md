## Changelog : fonds-prevention-argile (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de synchronisation des données, de statistiques, de sécurité et de l'expérience utilisateur. Une nouvelle fonctionnalité de synchronisation CRON a été mise en place pour la démarche de diagnostic, et des correctifs ont été apportés pour améliorer la sécurité et la précision des données affichées.

### Évolutions fonctionnelles
- Ajout du préremplissage du numéro de téléphone pour faciliter la saisie des informations. [#190](https://github.com/MTES-MCT/fonds-prevention-argile/issues/190)
- Intégration d'une source d'acquisition dans le modal d'inscription pour un meilleur suivi des utilisateurs. [#183](https://github.com/MTES-MCT/fonds-prevention-argile/issues/183)
- Ajout de statistiques sur les demandeurs accessibles aux analystes. [#182](https://github.com/MTES-MCT/fonds-prevention-argile/issues/182)
- Mise en place d'un graphique pour visualiser l'évolution du nombre d'utilisateurs. [#184](https://github.com/MTES-MCT/fonds-prevention-argile/issues/184)
- Ajout d'une démarche DN Diagnostic. [#173](https://github.com/MTES-MCT/fonds-prevention-argile/issues/173)
- Intégration d'un nouvel arrêté. [#170](https://github.com/MTES-MCT/fonds-prevention-argile/issues/170) et [#179](https://github.com/MTES-MCT/fonds-prevention-argile/issues/179)
- Amélioration des libellés dans l'interface utilisateur. [#181](https://github.com/MTES-MCT/fonds-prevention-argile/issues/181) et [#175](https://github.com/MTES-MCT/fonds-prevention-argile/issues/175)

### Évolutions techniques
- Mise en place d'un CRON pour la synchronisation des données, améliorant l'automatisation et la fiabilité du processus. [#189](https://github.com/MTES-MCT/fonds-prevention-argile/issues/189)
- Correction d'une vulnérabilité IDOR (Insecure Direct Object Reference) en ajoutant une vérification de l'accès au territoire. [#186](https://github.com/MTES-MCT/fonds-prevention-argile/issues/186)
- Amélioration de la performance et de la gestion de la mémoire grâce à la mémoïsation et la mise à jour des statistiques. [#168](https://github.com/MTES-MCT/fonds-prevention-argile/issues/168)
- Refonte des statistiques et du script associé. [#169](https://github.com/MTES-MCT/fonds-prevention-argile/issues/169)
- Correction d'un problème avec le rendu initial de Matomo dans le simulateur. [#171](https://github.com/MTES-MCT/fonds-prevention-argile/issues/171)
- Correction d'un bug dans le calcul des statistiques. [#176](https://github.com/MTES-MCT/fonds-prevention-argile/issues/176)
- Correction d'un problème lié à l'endpoint pour l'exécution après une action. [#191](https://github.com/MTES-MCT/fonds-prevention-argile/issues/191)
- Correction de bugs divers. [#187](https://github.com/MTES-MCT/fonds-prevention-argile/issues/187) et [#188](https://github.com/MTES-MCT/fonds-prevention-argile/issues/188)

### Autres changements
- Mise à jour des dépendances. [#172](https://github.com/MTES-MCT/fonds-prevention-argile/issues/172)
- Correction du contenu JSON de la page d'accueil. [#185](https://github.com/MTES-MCT/fonds-prevention-argile/issues/185)
- Bump de la version à v1.10.0. [#180](https://github.com/MTES-MCT/fonds-prevention-argile/issues/180)
- Rétractation temporaire de l'intégration du nouvel arrêté suite à un problème. [#174](https://github.com/MTES-MCT/fonds-prevention-argile/issues/174)
