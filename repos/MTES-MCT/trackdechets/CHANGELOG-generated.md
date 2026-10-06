## Changelog : trackdechets (30 derniers jours, au 22 septembre 2026)

### Résumé
Cette période a été principalement consacrée au renforcement de la sécurité de la plateforme (protection contre les injections et les fuites de données) et à l'amélioration de l'expérience utilisateur. Des corrections importantes ont été apportées sur l'affichage mobile, la génération des documents PDF et la fiabilité des bordereaux (BSFF).

### Évolutions fonctionnelles
- **Interface utilisateur & Mobile** :
    - Correction d'un problème d'affichage sur mobile où le bouton d'aide « ? » masquait l'onglet « Signer » [#4898](https://github.com/MTES-MCT/trackdechets/issues/4898).
    - Simplification de la bannière par la suppression du bouton et de la redirection [#4894](https://github.com/MTES-MCT/trackdechets/issues/4894).
- **Gestion des bordereaux (BSFF)** :
    - Ajout de l'onglet transporteur dans l'aperçu des bordereaux [#4883](https://github.com/MTES-MCT/trackdechets/issues/4883).
    - Automatisation du renseignement de l'opération réalisée et de la date de traitement dès la réception du bordereau [#4884](https://github.com/MTES-MCT/trackdechets/issues/4884).
- **Corrections de bugs** :
    - Résolution d'un problème empêchant la suppression d'un transporteur lorsqu'il était déjà présent dans le BSD [#4897](https://github.com/MTES-MCT/trackdechets/issues/4897).
    - Correction du type de quantité dans les PDF qui restait systématiquement en "réelle" même en cas de valeur de réception indéfinie [#4857](https://github.com/MTES-MCT/trackdechets/issues/4857).

### Évolutions techniques
- **Sécurité** :
    - Correction d'une vulnérabilité de type SSRF (falsification de requête côté serveur) via l'URI "endpointUri" des webhooks [#4904](https://github.com/MTES-MCT/trackdechets/issues/4904).
    - Travaux sur la protection des données personnelles (email, téléphone, nom, prénom) pour éviter leur récupération via l'API pour les établissements publics [#4899](https://github.com/MTES-MCT/trackdechets/issues/4899).
    - Ajout d'une option `maxRedirect` pour sécuriser les redirections non autorisées.
- **Infrastructure & CI/CD** :
    - Déploiement et correction de la configuration de Crisp et Minio sur les environnements de production et de sandbox [#4892](https://github.com/MTES-MCT/trackdechets/issues/4892).
    - Correction des URLs de buildpacks en supprimant le suffixe `.git` [#4903](https://github.com/MTES-MCT/trackdechets/issues/4903).
- **Workflow** :
    - Correction du processus de validation des doublos pour les BSVHU.
