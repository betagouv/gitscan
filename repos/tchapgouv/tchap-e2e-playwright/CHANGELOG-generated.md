## Changelog : tchap-e2e-playwright (30 derniers jours, au 30 octobre 2026)

### Résumé
Les récentes mises à jour visent à renforcer la fiabilité des tests de bout en bout en couvrant de nouveaux scénarios d'authentification et de gestion de comptes. Le projet assure également la compatibilité avec la version 4.23.0-rc.1 de Tchap et optimise la rapidité d'exécution de la suite de tests.

### Évolutions fonctionnelles
- Extension de la couverture de tests pour inclure les cas de discordance d'e-mail via le protocole OIDC.
- Ajout de tests concernant l'envoi d'e-mails pour les comptes désactivés ne possédant pas d'adresse e-mail [#64](https://github.com/tchapgouv/tchap-e2e-playwright/pull/64).
- Correction des tests relatifs aux salons privés sécurisés.
- Mise à jour de la suite de tests "web minimal" pour assurer la compatibilité avec la version tchap-4.23.0-rc.1 [#66](https://github.com/tchapgouv/tchap-e2e-playwright/pull/66).

### Évolutions techniques
- Optimisation de la performance en réduisant les délais d'attente (timeouts) par test.
