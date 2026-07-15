## Changelog : lab-anssi-antivirus (30 derniers jours, au 13 juillet 2026)

### Résumé
Ce mois-ci, le projet a fait des avancées significatives dans la sécurisation des communications avec le service d'antivirus. L'implémentation de TLS (chiffrement) et l'authentification par certificat renforcent la protection des données transmises, tout en améliorant la robustesse et la testabilité du code.

### Évolutions fonctionnelles
- **Sécurisation des communications :** Implémentation du chiffrement TLS pour sécuriser la communication avec le daemon ClamAV.
- **Authentification par certificat :**  Le trafic du client est maintenant authentifié via un certificat, renforçant la sécurité.
- **Nom de certificat configurable :** Possibilité de spécifier le nom couvert par le certificat utilisé pour la communication TLS.
- **Script de lancement :** Ajout d'un script pour faciliter le lancement du service.

### Évolutions techniques
- **Infrastructure Nix :** Initialisation du projet avec Nix pour une gestion des dépendances et une reproductibilité améliorées.
- **Tests :**
    - Simulation du daemon `clamd` pour faciliter les tests.
    - Amélioration de la validation des tests, notamment en vérifiant le rejet du trafic avec un mauvais certificat.
    - Suppression de duplication et nettoyage du code dans les tests.
    - Désactivation d'avertissements inutiles dans les tests.
- **Refactoring :**
    - Extraction du code spécifique à la gestion des clés et certificats.
    - Déduplication de code dans les tests.
    - Suppression de variables globales.
- **Qualité du code :** Ajout de `shellcheck` pour l'analyse statique du code shell.
- **Dépendances :** Explicitation des dépendances du projet.

### Autres changements
- Documentation de la partie client.
