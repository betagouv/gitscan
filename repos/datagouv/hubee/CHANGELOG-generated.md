## Changelog : hubee (30 derniers jours, au 03 novembre 2026)

### Résumé
Les récentes évolutions de hubee se concentrent sur l'amélioration de l'expérience utilisateur du portail (gestion des agents, abonnements et suivi des dossiers) et sur un renforcement majeur de la sécurité et de la traçabilité grâce à une gestion plus fine des journaux d'activité et des correctifs de vulnérabilités.

### Évolutions fonctionnelles
- **Gestion des agents** : Amélioration de la visibilité avec la possibilité de lister les agents d'une organisation, d'afficher leurs champs détaillés et de suivre leur dernière date de connexion.
- **Suivi des dossiers et flux** : Nommage plus explicite des flux dans la liste des télédossiers et ajout de la possibilité de marquer un dossier comme "lu".
- **Communication et archivage** : Mise en place de messages adressés directement aux agents lors des changements d'état d'un dossier et création d'un système d'archivage pour les pièces jointes ajoutées.
- **Gestion des abonnements** : Ajout de la consultation de la liste des abonnements de la structure.
- **Interface utilisateur** : Amélioration de la navigation (menu), ajout d'un bandeau d'information sur la phase bêta et corrections typographiques.

### Évolutions techniques
- **Sécurité** : Correction de plusieurs vulnérabilités (CVE) et renforcement de la confidentialité en masquant les données sensibles (nonces, adresses, noms de fichiers) dans les journaux d'activité.
- **API** : Standardisation des réponses de l'API pour garantir un format JSON systématique, même en cas d'erreur ou de route inconnue, et sécurisation de la lecture des jetons d'authentification.
- **Observabilité et Logs** : Optimisation de la journalisation pour inclure l'adresse IP des appelants et une meilleure gestion des exceptions et des redirections.
- **Infrastructure et CI/CD** : Mise à jour de l'environnement Ruby, optimisation des images Docker (utilisation de versions *distroless*) et amélioration des *review apps* (intégration de Sentry et gestion de la file d'attente Solid Queue).
- **Tests** : Renforcement de la couverture de tests de bout en bout, notamment sur la gestion des agents et l'archivage des pièces.

### Autres changements
- **Documentation** : Précisions apportées sur les processus de rattachement des agents lors de l'authentification.
- **Développement** : Ajout de tâches de préparation de données (*seeds*) pour faciliter l'enrôlement de comptes de test.
