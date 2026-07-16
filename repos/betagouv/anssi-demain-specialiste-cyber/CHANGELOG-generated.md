## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce changelog fait état d'une période axée sur la sécurité du projet. Des mesures ont été prises pour renforcer la sécurité de la chaîne d'approvisionnement (CI/CD) et du code source, notamment en désactivant les identifiants Git et en corrigeant une vulnérabilité potentielle d'injection de code. L'intégration de Renovate a également été finalisée pour automatiser les mises à jour de dépendances.

### Évolutions techniques
- Renforcement de la sécurité de la chaîne CI/CD :
  - Désactivation des identifiants Git dans les dépôts clonés [#7972f7d](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/7972f7d)
  - Validation des configurations dans la CI [#0d77e09](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/0d77e09)
- Correction d'une vulnérabilité potentielle d'injection de code par 'template expansion' [#096bae2](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/096bae2)
- Intégration de Renovate pour la gestion automatisée des dépendances :
  - Configuration initiale de Renovate [#fb2fc24](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/fb2fc24)
  - Ajout du fichier de configuration Renovate [#badb3ea](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/badb3ea)
- Épinglage des versions des dépendances utilisées dans les GitHub Actions [#c58addd](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/c58addd)

### Autres changements
- Mises à jour de dépendances (sécurité et versions récentes) :
  - Mise à jour de `vitest` vers la version 3.2.6 (correction de sécurité)
  - Mise à jour de `multer` vers la version 2.2.0 (correction de sécurité)
  - Mise à jour de `qs` vers la version ~6.15.0 (correction de sécurité)
  - Mise à jour de `@lab-anssi/lib` vers la version 2.1.7
  - Mise à jour de `express` vers la version 4.22.2
  - Mise à jour de `brace-expansion` vers la version 1.1.15
  - Mise à jour de `minimatch` vers les versions 9.0.9 et 3.1.5
