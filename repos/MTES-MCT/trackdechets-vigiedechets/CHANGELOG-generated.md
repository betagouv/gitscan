## Changelog : trackdechets-vigiedechets (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité (limitation des tentatives de réinitialisation de mot de passe), l'export des données du registre par SIREN/SIRET, l'amélioration de l'expérience utilisateur avec des messages d'aide dynamiques et la résolution de problèmes liés à la configuration CORS et des referrers. Des mises à jour de l'image MinIO ont également été effectuées.

### Évolutions fonctionnelles
- Possibilité d'exporter le registre par SIREN ou SIRET. [#469](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/469)
- Ajout de messages d'aide dynamiques pour le type de registre, améliorant la clarté pour l'utilisateur. [#463](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/463)
- Déblocage de la sentinelle et ajout d'une aide concernant la sandbox pour faciliter l'utilisation de l'environnement de test. [#468](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/468)

### Évolutions techniques
- Limitation du nombre de tentatives de réinitialisation de mot de passe pour renforcer la sécurité. [#472](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/472)
- Mise à jour de l'image MinIO utilisée dans les workflows pour bénéficier des dernières corrections et améliorations. [#473](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/473)
- Correction de la configuration CORS et ajout du referrer pour résoudre des problèmes de compatibilité et de sécurité. [#461](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/461)

### Autres changements
- Amélioration du processus de téléchargement du client MinIO.
- Reformattage des tests de la vue `accounts`.
- Diverses corrections et améliorations internes.
