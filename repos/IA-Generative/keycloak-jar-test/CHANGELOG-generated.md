## Changelog : keycloak-jar-test (30 derniers jours, au 02 septembre 2026)

### Résumé
Cette période a été marquée par un renforcement significatif de la sécurité pour l'intégration ProConnect, notamment grâce à l'introduction de l'authentification à deux facteurs (2FA) et une meilleure gestion des niveaux de sécurité eIDAS.

### Évolutions fonctionnelles
- **Amélioration de la sécurité ProConnect** : Activation de l'authentification à deux facteurs (2FA) pour l'identité ProConnect.
- **Gestion fine de la 2FA** : Introduction de trois modes de fonctionnement pour la double authentification : Désactivé (DISABLED), Optionnel (OPTIONAL) et Requis (REQUIRED).
- **Optimisation des niveaux d'accès** : Utilisation des nouvelles revendications (claims) ACR dans le processus 2FA et amélioration de la prise en charge du niveau d'authentification "eIDAS0" pour ProConnect.

### Évolutions techniques
- **CI/CD** : Automatisation de la récupération des builds en configurant l'upload du fichier JAR compilé en tant qu'artefact de workflow.
- **Tests** : Correction des tests de l'authentification multi-facteurs (MFA) pour assurer la stabilité des tests d'identité (IdP) et de la gestion des valeurs par défaut ACR.

### Autres changements
- **Documentation** : Ajout de guides sur l'activation de la 2FA ProConnect et ses limites de compatibilité.
- **Documentation** : Ajout d'une capture d'écran de l'interface d'administration pour faciliter la configuration de la 2FA ProConnect.
