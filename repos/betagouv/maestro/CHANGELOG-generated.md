## Changelog : maestro (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Maestro se concentrent sur l'amélioration de la gestion des laboratoires, des prélèvements et des analyses, notamment en lien avec les exigences SEVES et Cereco. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience utilisateur. L'application continue d'être stabilisée et optimisée avec des mises à jour régulières des dépendances.

### Évolutions fonctionnelles
- **Laboratoires:** Ajout d'une interface de configuration des laboratoires, permettant une gestion plus fine de leurs paramètres et de leurs agréments [#871](https://github.com/betagouv/maestro/issues/871).
- **SEVES:** Implémentation d'une API dédiée à l'échange de données avec le système SEVES [#900](https://github.com/betagouv/maestro/issues/900).
- **Cereco:** Prise en compte des LMR non quantifiables dans le cadre de l'intégration avec Cereco [#938](https://github.com/betagouv/maestro/issues/938).
- **DAI:** Possibilité de repasser des DAI en erreur pour permettre leur relance [#1063](https://github.com/betagouv/maestro/issues/1063).
- **Prélèvements:** Ajout d'un filtre par département pour les administrations centrales [#937](https://github.com/betagouv/maestro/issues/937).
- **Documents:** Autorisation du dépôt de documents pour le suivi national [#1051](https://github.com/betagouv/maestro/issues/1051).
- **Sacha:** Séparation des emails pour l'EDI Sacha [#1062](https://github.com/betagouv/maestro/issues/1062) et ajout de l'identifiant de l'acteur [#1057](https://github.com/betagouv/maestro/issues/1057).
- **DAOA:** Possibilité d'imprimer le formulaire vierge qu'après la sélection de l'abattoir [#1011](https://github.com/betagouv/maestro/issues/1011).

### Évolutions techniques
- **API:** Amélioration du typage des réponses de l'API pour une meilleure robustesse et une meilleure expérience développeur [#1006](https://github.com/betagouv/maestro/issues/1006).
- **Zod:** Gestion des réponses non définies via Zod pour une meilleure validation des données [#966](https://github.com/betagouv/maestro/issues/966).
- **URL Builder:** Ajout d'un builder d'URL typé pour faciliter la construction d'URL valides et cohérentes [#987](https://github.com/betagouv/maestro/issues/987).
- **Nodemailer:** Utilisation d'une meilleure méthode pour ajouter les pièces jointes lors de l'envoi d'emails [#991](https://github.com/betagouv/maestro/issues/991).
- **GPG:** Passage en mode non interactif pour les opérations GPG [#938](https://github.com/betagouv/maestro/issues/938).
- **Refactoring:** Remplacement de `swc` par `node` pour certaines tâches de build [#1037](https://github.com/betagouv/maestro/issues/1037).
- **Mises à jour:** Mises à jour de nombreuses dépendances (React, Node.js, PostgreSQL, S3, Browserless, Dex, etc.) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.

### Autres changements
- **Alertes Mattermost:** Envoi d'une alerte Mattermost en cas de problème lors de l'envoi d'un email via Brevo [#1056](https://github.com/betagouv/maestro/issues/1056).
- **Corrections:** Correction de la génération des anciennes étiquettes [#1065](https://github.com/betagouv/maestro/issues/1065) et correction de l'affichage du dashboard en cas de changement de plan [#1064](https://github.com/betagouv/maestro/issues/1064).
- **Documentation:** Amélioration de la documentation interne et correction de quelques balises [#1044](https://github.com/betagouv/maestro/issues/1044).
- **Tests:** Ajout et mise à jour de tests unitaires et d'intégration.
- **Divers:** Correction de divers bugs mineurs et améliorations de l'interface utilisateur.
