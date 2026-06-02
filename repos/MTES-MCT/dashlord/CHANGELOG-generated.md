## Changelog : dashlord (30 derniers jours, au 31 mai 2026)

### Résumé
Ce changelog fait état d'une mise à jour importante de la liste des sites web surveillés par Dashlord. De nombreux liens vers des services gouvernementaux ont été mis à jour ou ajoutés, améliorant ainsi la couverture de l'outil et sa capacité à surveiller la sécurité de ces plateformes. Une maintenance a également été effectuée sur la configuration de l'outil.

### Évolutions fonctionnelles
- Mise à jour des URLs de plusieurs sites web surveillés, incluant notamment : Pitchou, MesAds, Boris, Vigieau, ZLV, Dialog, Zero Logement Vacant, Emile, Ecobalyse, Transport Data, Track Déchets, Oilhi, Mondo Gartif, Resorption Bidonvilles, Prélevements d'Eau, Potentiel, Partaj, Mission Transition, Mon Devis Sans Oublis, Mobilic, Le Taxi, Stop Punaises, Signal Logement, Haie, Envergo, France Chaleur Urbaine, Filigrane, Dossier Facile (plusieurs URLs), Covoiturage (plusieurs URLs), Carbure, Camino, Aquapreneur, Aides Territoires, Acces Libre et Apilos Logement.
- Ajout des sites Prelex et Emile (vers l'application) à la liste des sites surveillés [#45](https://github.com/MTES-MCT/dashlord/pull/45).

### Évolutions techniques
- Mise à jour de l'URL de l'API dans le fichier `dashlord.yml`.
- Suppression de l'entrée a-dock du fichier `dashlord.yml`.
- Ajustement de la configuration de Dashlord : désactivation des statistiques, du budget, de Dependabot, de Codescan et de Betagouv pour Prelex.

### Autres changements
- Mise à jour régulière du rapport de l'outil (plusieurs occurrences).
